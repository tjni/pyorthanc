from datetime import datetime
from typing import Dict, List

from httpx import ReadTimeout

from .resource import Resource
from .series import Series
from .. import errors, util
from ..jobs import Job


class Study(Resource):
    """Represent a study that is in an Orthanc server

    This object has many getters that allow the user to retrieve metadata
    or the entire DICOM file of the Series
    """

    def get_main_information(self) -> Dict:
        """Get Study information

        Returns
        -------
        Dict
            Dictionary of study information
        """
        if self.lock:
            if self._information is None:
                # Setup self._information for the first time when study is lock
                self._information = self.client.get_studies_id(self.id_)

            return self._information

        return self.client.get_studies_id(self.id_)

    @property
    def referring_physician_name(self) -> str:
        """Get referring physician name"""
        return self._get_main_dicom_tag_value('ReferringPhysicianName')

    @property
    def requesting_physician(self) -> str:
        """Get referring physician name"""
        return self._get_main_dicom_tag_value('RequestingPhysician')

    @property
    def date(self) -> datetime:
        """Get study date

        The date have precision to the second (if available).

        Returns
        -------
        datetime
            Study date
        """
        date_string = self._get_main_dicom_tag_value('StudyDate')
        try:
            time_string = self._get_main_dicom_tag_value('StudyTime')
        except errors.TagDoesNotExistError:
            time_string = None

        return util.make_datetime_from_dicom_date(date_string, time_string)

    @property
    def study_id(self) -> str:
        """Get Study ID"""
        return self._get_main_dicom_tag_value('StudyID')

    @property
    def uid(self) -> str:
        """Get StudyInstanceUID"""
        return self._get_main_dicom_tag_value('StudyInstanceUID')

    @property
    def patient_identifier(self) -> str:
        """Get the Orthanc identifier of the parent patient"""
        return self.get_main_information()['ParentPatient']

    @property
    def patient_information(self) -> Dict:
        """Get patient information"""
        return self.get_main_information()['PatientMainDicomTags']

    @property
    def series(self) -> List[Series]:
        """Get Study series"""
        if self.lock:
            if self._child_resources is None:
                series_ids = self.get_main_information()['Series']
                self._child_resources = [Series(i, self.client, self.lock) for i in series_ids]

            return self._child_resources

        series_ids = self.get_main_information()['Series']

        return [Series(i, self.client, self.lock) for i in series_ids]

    @property
    def accession_number(self) -> str:
        return self._get_main_dicom_tag_value('AccessionNumber')

    @property
    def description(self) -> str:
        return self._get_main_dicom_tag_value('StudyDescription')

    @property
    def institution_name(self) -> str:
        return self._get_main_dicom_tag_value('InstitutionName')

    @property
    def requested_procedure_description(self) -> str:
        return self._get_main_dicom_tag_value('RequestedProcedureDescription')

    @property
    def is_stable(self) -> bool:
        return self.get_main_information()['IsStable']

    @property
    def last_update(self) -> datetime:
        last_updated_date_and_time = self.get_main_information()['LastUpdate'].split('T')
        date = last_updated_date_and_time[0]
        time = last_updated_date_and_time[1]

        return util.make_datetime_from_dicom_date(date, time)

    @property
    def labels(self) -> List[str]:
        return self.get_main_information()['Labels']

    def add_label(self, label: str) -> None:
        self.client.put_studies_id_labels_label(self.id_, label)

    def remove_label(self, label):
        self.client.delete_studies_id_labels_label(self.id_, label)

    def anonymize(self, remove: List = None, replace: Dict = None, keep: List = None,
                  force: bool = False, keep_private_tags: bool = False,
                  keep_source: bool = True, priority: int = 0, permissive: bool = False,
                  dicom_version: str = None) -> 'Study':
        """Anonymize study

        If no error has been raise, return an anonymous study.
        Documentation: https://book.orthanc-server.com/users/anonymization.html

        Notes
        -----
        This method might be long to run, especially on large study or when multiple
        studys are anonymized. In those cases, it is recommended to use the `.anonymize_as_job()`

        Parameters
        ----------
        remove
            List of tag to remove
        replace
            Dictionary of {tag: new_content}
        keep
            List of tag to keep unchanged
        force
            Some tags can't be changed without forcing it (e.g. StudyID) for security reason
        keep_private_tags
            If True, keep the private tags from the DICOM instances.
        keep_source
            If False, instructs Orthanc to the remove original resources.
            By default, the original resources are kept in Orthanc.
        priority
            In asynchronous mode, the priority of the job. The lower the value, the higher the priority.
        permissive
            If True, ignore errors during the individual steps of the job.
        dicom_version
            Version of the DICOM standard to be used for anonymization.
            Check out configuration option DeidentifyLogsDicomVersion for possible values.

        Returns
        -------
        Study
            A New anonymous study.

        Examples
        --------
        ```python
        new_study = study.anonymize()

        new_study_with_specific_study_id = study.anonymize(
            replace={'StudyDescription': 'A description'}
        )
        """
        remove = [] if remove is None else remove
        replace = {} if replace is None else replace
        keep = [] if keep is None else keep

        data = {
            'Asynchronous': False,
            'Remove': remove,
            'Replace': replace,
            'Keep': keep,
            'Force': force,
            'KeepPrivateTags': keep_private_tags,
            'KeepSource': keep_source,
            'Priority': priority,
            'Permissive': permissive,
        }
        if dicom_version is not None:
            data['DicomVersion'] = dicom_version

        try:
            anonymous_study = self.client.post_studies_id_anonymize(self.id_, data)
        except ReadTimeout:
            raise ReadTimeout(
                'Study anonymization is too long to process. '
                'Use `.anonymize_as_job` or increase client.timeout.'
            )

        return Study(anonymous_study['ID'], self.client)

    def anonymize_as_job(self, remove: List = None, replace: Dict = None, keep: List = None,
                         force: bool = False, keep_private_tags: bool = False,
                         keep_source: bool = True, priority: int = 0, permissive: bool = False,
                         dicom_version: str = None) -> Job:
        """Anonymize study and return a job

        Launch an anonymization job.
        Documentation: https://book.orthanc-server.com/users/anonymization.html

        Notes
        -----
        This method is useful when anonymizing large study or launching many
        anonymization jobs. The jobs are sent to Orthanc and processed according
        to the priority.

        Parameters
        ----------
        remove
            List of tag to remove
        replace
            Dictionary of {tag: new_content}
        keep
            List of tag to keep unchanged
        force
            Some tags can't be changed without forcing it (e.g. PatientID) for security reason
        keep_private_tags
            If True, keep the private tags from the DICOM instances.
        keep_source
            If False, instructs Orthanc to the remove original resources.
            By default, the original resources are kept in Orthanc.
        priority
            In asynchronous mode, the priority of the job. The lower the value, the higher the priority.
        permissive
            If True, ignore errors during the individual steps of the job.
        dicom_version
            Version of the DICOM standard to be used for anonymization.
            Check out configuration option DeidentifyLogsDicomVersion for possible values.

        Returns
        -------
        Job
            Return a Job object of the anonymization job.

        Examples
        --------
        For large study (recommended)
        ```python
        job = study.anonymize_as_job(asynchronous=True)
        job.state  # You can follow the job state

        job.wait_until_completion() # Or just wait on its completion
        new_study = Patient(job.content['ID'], orthanc)
        ```
        """
        remove = [] if remove is None else remove
        replace = {} if replace is None else replace
        keep = [] if keep is None else keep

        data = {
            'Asynchronous': True,
            'Remove': remove,
            'Replace': replace,
            'Keep': keep,
            'Force': force,
            'KeepPrivateTags': keep_private_tags,
            'KeepSource': keep_source,
            'Priority': priority,
            'Permissive': permissive,
        }
        if dicom_version is not None:
            data['DicomVersion'] = dicom_version

        job_info = self.client.post_studies_id_anonymize(self.id_, data)

        return Job(job_info['ID'], self.client)

    def get_zip(self) -> bytes:
        """Get the bytes of the zip file

        Get the .zip file.

        Returns
        -------
        bytes
            Bytes of Zip file of the study.

        Examples
        --------
        ```python
        from pyorthanc import Orthanc, Study
        a_study = Study(
            'STUDY_IDENTIFIER',
            Orthanc('http://localhost:8042')
        )
        bytes_content = a_study.get_zip()
        with open('study_zip_file_path.zip', 'wb') as file_handler:
            file_handler.write(bytes_content)
        ```

        """
        return self.client.get_studies_id_archive(self.id_)

    def remove_empty_series(self) -> None:
        """Delete empty series."""
        if self._child_resources is None:
            return

        for series in self._child_resources:
            series.remove_empty_instances()

        self._child_resources = [series for series in self._child_resources if series._child_resources != []]
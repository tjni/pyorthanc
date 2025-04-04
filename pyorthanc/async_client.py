import warnings
from typing import Any, Dict, Optional, List, Union

import httpx
from httpx._types import (
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
)


class AsyncOrthanc(httpx.AsyncClient):
    """Orthanc API

    version 1.12.6
    This is the full documentation of the [REST API](https://orthanc.uclouvain.be/book/users/rest.html) of Orthanc.<p>This reference is automatically generated from the source code of Orthanc. A [shorter cheat sheet](https://orthanc.uclouvain.be/book/users/rest-cheatsheet.html) is part of the Orthanc Book.<p>An earlier, manually crafted version from August 2019, is [still available](2019-08-orthanc-openapi.html), but is not up-to-date anymore ([source](https://groups.google.com/g/orthanc-users/c/NUiJTEICSl8/m/xKeqMrbqAAAJ)).

    """

    def __init__(
        self,
        url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        return_raw_response: bool = False,
        *args,
        **kwargs,
    ):
        """
        Parameters
        ----------
        url
            server's URL
        username
            Orthanc's username
        password
            Orthanc's password
        return_raw_response
            All Orthanc's methods will return a raw httpx.Response rather than the serialized result
        *args, **kwargs
            Parameters passed to the httpx.Client (headers, timeout, etc.)
        """
        super().__init__(*args, **kwargs)
        self.url = url
        self.version = "1.12.6"
        self.return_raw_response = return_raw_response

        if username and password:
            self.setup_credentials(username, password)

    def setup_credentials(self, username: str, password: str) -> None:
        """Set credentials needed for HTTP requests"""
        self._auth = httpx.BasicAuth(username, password)

    async def _get(
        self,
        route: str,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """GET request with specified route

        Parameters
        ----------
        route
            HTTP route.
        params
            Parameters for the HTTP request.
        headers
            Headers for the HTTP request.
        cookies

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Serialized response of the HTTP GET request or httpx.Response.
        """
        response = await self.get(
            url=route, params=params, headers=headers, cookies=cookies
        )

        if self.return_raw_response:
            return response

        if 200 <= response.status_code < 300:
            if "application/json" in response.headers["content-type"]:
                return response.json()
            elif "text/plain" in response.headers["content-type"]:
                return response.text
            else:
                return response.content

        raise httpx.HTTPError(
            f"HTTP code: {response.status_code}, with content: {response.text}"
        )

    async def _delete(
        self,
        route: str,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """DELETE to specified route

        Parameters
        ----------
        route
            HTTP route.
        params
            Parameters for the HTTP request.
        headers
            Headers for the HTTP request.
        cookies

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Serialized response of the HTTP DELETE request or httpx.Response.
        """
        response = await self.delete(
            route, params=params, headers=headers, cookies=cookies
        )

        if self.return_raw_response:
            return response

        if 200 <= response.status_code < 300:
            if "application/json" in response.headers["content-type"]:
                return response.json()
            elif "text/plain" in response.headers["content-type"]:
                return response.text
            else:
                return response.content

        raise httpx.HTTPError(
            f"HTTP code: {response.status_code}, with content: {response.text}"
        )

    async def _post(
        self,
        route: str,
        content: Optional[RequestContent] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """POST to specified route

        Parameters
        ----------
        route
            HTTP route.
        content
        data
            Dictionary to send in the body of request.
        files
        json
        params
        headers
        cookies

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Serialized response of the HTTP POST request or httpx.Response.
        """
        response = await self.post(
            route,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
        )

        if self.return_raw_response:
            return response

        if 200 <= response.status_code < 300:
            if "application/json" in response.headers["content-type"]:
                return response.json()
            elif "text/plain" in response.headers["content-type"]:
                return response.text
            else:
                return response.content

        raise httpx.HTTPError(
            f"HTTP code: {response.status_code}, with text: {response.text}"
        )

    async def _put(
        self,
        route: str,
        content: RequestContent = None,
        data: RequestData = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """PUT to specified route

        Parameters
        ----------
        route
            HTTP route.
        content
        data
            Dictionary to send in the body of request.
        files
        json
        params
        headers
        cookies

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Serialized response of the HTTP PUT request or httpx.Response.
        """
        response = await self.put(
            route,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
        )

        if self.return_raw_response:
            return response

        if 200 <= response.status_code < 300:
            if "application/json" in response.headers["content-type"]:
                return response.json()
            elif "text/plain" in response.headers["content-type"]:
                return response.text
            else:
                return response.content

        raise httpx.HTTPError(
            f"HTTP code: {response.status_code}, with text: {response.text}"
        )

    async def delete_changes(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Clear changes

        Clear the full history stored in the changes log
        Tags: Tracking changes

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/changes",
        )

    async def get_changes(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List changes

        Whenever Orthanc receives a new DICOM instance, this event is recorded in the so-called _Changes Log_. This enables remote scripts to react to the arrival of new DICOM resources. A typical application is auto-routing, where an external script waits for a new DICOM instance to arrive into Orthanc, then forward this instance to another modality. Please note that, when resources are deleted, their corresponding change entries are also removed from the Changes Log, which helps ensuring that this log does not grow indefinitely.
        Tags: Tracking changes

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "last" (float): Request only the last change id (this argument must be used alone)
                "limit" (float): Limit the number of results
                "since" (float): Show only the resources since the provided index excluded
                "to" (float): Show only the resources till the provided index included (only available if your DB backend supports ExtendedChanges)
                "type" (str): Show only the changes of the provided type (only available if your DB backend supports ExtendedChanges).  Multiple values can be provided and must be separated by a ';'.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The list of changes
        """
        return await self._get(
            route=f"{self.url}/changes",
            params=params,
        )

    async def delete_exports(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Clear exports

        Clear the full history stored in the exports log
        Tags: Tracking changes

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/exports",
        )

    async def get_exports(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List exports

        For medical traceability, Orthanc can be configured to store a log of all the resources that have been exported to remote modalities. In auto-routing scenarios, it is important to prevent this log to grow indefinitely as incoming instances are routed. You can either disable this logging by setting the option `LogExportedResources` to `false` in the configuration file, or periodically clear this log by `DELETE`-ing this URI. This route might be removed in future versions of Orthanc.
        Tags: Tracking changes

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "limit" (float): Limit the number of results
                "since" (float): Show only the resources since the provided index

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The list of exports
        """
        return await self._get(
            route=f"{self.url}/exports",
            params=params,
        )

    async def get_instances(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List the available instances

        List the Orthanc identifiers of all the available DICOM instances
        Tags: Instances

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual resources, not only their Orthanc identifiers
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "limit" (float): Limit the number of results
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "response-content" (str): Defines the content of response for each returned resource.  Allowed values are `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`, `Attachments`.  If not specified, Orthanc will return `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`.e.g: 'response-content=MainDicomTags;Children (new in Orthanc 1.12.5 - overrides `expand`)
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "since" (float): Show only the resources since the provided index

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the Orthanc identifiers, or detailed information about the reported instances (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/instances",
            params=params,
        )

    async def post_instances(
        self,
        content: RequestContent = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Upload DICOM instances

        Upload DICOM instances
        Tags: Instances

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the uploaded instance, or list of information for each uploaded instance in the case of ZIP archive
        """
        return await self._post(
            route=f"{self.url}/instances",
            content=content,
        )

    async def delete_instances_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete some instance

        Delete the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/instances/{id_}",
        )

    async def get_instances_id(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get information about some instance

        Get detailed information about the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM instance
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}",
            params=params,
        )

    async def post_instances_id_anonymize(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Anonymize instance

        Download an anonymized version of the DICOM instance whose Orthanc identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/anonymization.html#anonymization-of-a-single-instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        json
            Dictionary with the following keys:
              "DicomVersion": Version of the DICOM standard to be used for anonymization. Check out configuration option `DeidentifyLogsDicomVersion` for possible values.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": List of DICOM tags whose value must not be destroyed by the anonymization. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepPrivateTags": Keep the private tags from the DICOM instances (defaults to `false`)
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of additional tags to be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The anonymized DICOM instance
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/instances/{id_}/anonymize",
            json=json,
        )

    async def get_instances_id_attachments(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List attachments

        Get the list of attachments that are associated with the given instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "full" (str): If present, retrieve the attachments list and their numerical ids

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the attachments
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments",
            params=params,
        )

    async def delete_instances_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete attachment

        Delete an attachment associated with the given DICOM instance. This call will fail if trying to delete a system attachment (i.e. whose index is < 1024).
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/instances/{id_}/attachments/{name}",
            headers=headers,
        )

    async def get_instances_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on attachments

        Get the list of the operations that are available for attachments associated with the given instance
        Tags: Other

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}",
            headers=headers,
        )

    async def put_instances_id_attachments_name(
        self,
        id_: str,
        name: str,
        content: RequestContent = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set attachment

        Attach a file to the given DICOM instance. This call will fail if trying to modify a system attachment (i.e. whose index is < 1024).
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        content
                - (Content-Type: "application/octet-stream") Binary data containing the attachment
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, if this is not the first time this attachment is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._put(
            route=f"{self.url}/instances/{id_}/attachments/{name}",
            content=content,
            headers=headers,
        )

    async def post_instances_id_attachments_name_compress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Compress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/instances/{id_}/attachments/{name}/compress",
        )

    async def get_instances_id_attachments_name_compressed_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment (no decompression)

        Get the (binary) content of one attachment associated with the given instance. The attachment will not be decompressed if `StorageCompression` is `true`.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/compressed-data",
            headers=headers,
        )

    async def get_instances_id_attachments_name_compressed_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment on disk

        Get the MD5 hash of one attachment associated with the given instance, as stored on the disk. This is different from `.../md5` iff `EnableStorage` is `true`.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/compressed-md5",
            headers=headers,
        )

    async def get_instances_id_attachments_name_compressed_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment on disk

        Get the size of one attachment associated with the given instance, as stored on the disk. This is different from `.../size` iff `EnableStorage` is `true`.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/compressed-size",
            headers=headers,
        )

    async def get_instances_id_attachments_name_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment

        Get the (binary) content of one attachment associated with the given instance
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/data",
            headers=headers,
        )

    async def get_instances_id_attachments_name_info(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get info about the attachment

        Get all the information about the attachment associated with the given instance
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the information about the attachment
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/info",
            headers=headers,
        )

    async def get_instances_id_attachments_name_is_compressed(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is attachment compressed?

        Test whether the attachment has been stored as a compressed file on the disk.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `0` if the attachment was stored uncompressed, `1` if it was compressed
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/is-compressed",
            headers=headers,
        )

    async def get_instances_id_attachments_name_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment

        Get the MD5 hash of one attachment associated with the given instance
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/md5",
            headers=headers,
        )

    async def get_instances_id_attachments_name_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment

        Get the size of one attachment associated with the given instance
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/attachments/{name}/size",
            headers=headers,
        )

    async def post_instances_id_attachments_name_uncompress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Uncompress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/instances/{id_}/attachments/{name}/uncompress",
        )

    async def post_instances_id_attachments_name_verify_md5(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Verify attachment

        Verify that the attachment is not corrupted, by validating its MD5 hash
        Tags: Instances

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            On success, a valid JSON object is returned
        """
        return await self._post(
            route=f"{self.url}/instances/{id_}/attachments/{name}/verify-md5",
        )

    async def get_instances_id_content_path(
        self,
        id_: str,
        path: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get raw tag

        Get the raw content of one DICOM tag in the hierarchy of DICOM dataset
        Tags: Instances

        Parameters
        ----------
        path
            Path to the DICOM tag. This is the interleaving of one DICOM tag, possibly followed by an index for sequences. Sequences are accessible as, for instance, `/0008-1140/1/0008-1150`
        id_
            Orthanc identifier of the DICOM instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The raw value of the tag of intereset (binary data, whose memory layout depends on the underlying transfer syntax), or JSON array containing the list of available tags if accessing a dataset
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/content/{path}",
        )

    async def post_instances_id_export(
        self,
        id_: str,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Write DICOM onto filesystem

        Write the DICOM file onto the filesystem where Orthanc is running.  This is insecure for Orthanc servers that are remotely accessible since one could overwrite any system file.  Since Orthanc 1.12.0, this route is disabled by default, but can be enabled using the `RestApiWriteToFileSystemEnabled` configuration option.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        data
            Target path on the filesystem

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/instances/{id_}/export",
            data=data,
        )

    async def get_instances_id_file(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Download DICOM

        Download one DICOM instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "transcode" (str): If present, the DICOM file will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html
        headers
            Dictionary of optional headers:
                "Accept" (str): This HTTP header can be set to retrieve the DICOM instance in DICOMweb format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The DICOM instance
            The DICOM instance, in DICOMweb JSON format
            The DICOM instance, in DICOMweb XML format
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/file",
            params=params,
            headers=headers,
        )

    async def get_instances_id_frames(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List available frames

        List the frames that are available in the DICOM instance of interest
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The list of the indices of the available frames
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames",
        )

    async def get_instances_id_frames_frame(
        self,
        frame: str,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations

        List the available operations under URI `/instances/{id}/frames/{frame}/`
        Tags: Other

        Parameters
        ----------
        frame

        id_


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}",
        )

    async def get_instances_id_frames_frame_image_int16(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode a frame (int16)

        Decode one frame of interest from the given DICOM instance. Pixels of grayscale images are truncated to the [-32768,32767] range. Negative values must be interpreted according to two's complement.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/image-int16",
            params=params,
            headers=headers,
        )

    async def get_instances_id_frames_frame_image_uint16(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode a frame (uint16)

        Decode one frame of interest from the given DICOM instance. Pixels of grayscale images are truncated to the [0,65535] range.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/image-uint16",
            params=params,
            headers=headers,
        )

    async def get_instances_id_frames_frame_image_uint8(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode a frame (uint8)

        Decode one frame of interest from the given DICOM instance. Pixels of grayscale images are truncated to the [0,255] range.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/image-uint8",
            params=params,
            headers=headers,
        )

    async def get_instances_id_frames_frame_matlab(
        self,
        frame: float,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode frame for Matlab

        Decode one frame of interest from the given DICOM instance, and export this frame as a Octave/Matlab matrix to be imported with `eval()`: https://orthanc.uclouvain.be/book/faq/matlab.html
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Octave/Matlab matrix
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/matlab",
        )

    async def get_instances_id_frames_frame_numpy(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode frame for numpy

        Decode one frame of interest from the given DICOM instance, for use with numpy in Python. The numpy array has 3 dimensions: (height, width, color channel).
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM resource of interest
        params
            Dictionary of optional parameters:
                "compress" (bool): Compress the file as `.npz`
                "rescale" (bool): On grayscale images, apply the rescaling and return floating-point values

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Numpy file: https://numpy.org/devdocs/reference/generated/numpy.lib.format.html
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/numpy",
            params=params,
        )

    async def get_instances_id_frames_frame_preview(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode a frame (preview)

        Decode one frame of interest from the given DICOM instance. The full dynamic range of grayscale images is rescaled to the [0,255] range.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/preview",
            params=params,
            headers=headers,
        )

    async def get_instances_id_frames_frame_raw(
        self,
        frame: float,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Access raw frame

        Access the raw content of one individual frame of the DICOM instance of interest, bypassing image decoding. This is notably useful to access the source files in compressed transfer syntaxes.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The raw frame
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/raw",
        )

    async def get_instances_id_frames_frame_raw_gz(
        self,
        frame: float,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Access raw frame (compressed)

        Access the raw content of one individual frame of the DICOM instance of interest, bypassing image decoding. This is notably useful to access the source files in compressed transfer syntaxes. The image is compressed using gzip
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The raw frame, compressed using gzip
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/raw.gz",
        )

    async def get_instances_id_frames_frame_rendered(
        self,
        frame: float,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Render a frame

        Render one frame of interest from the given DICOM instance. This function takes scaling into account (`RescaleSlope` and `RescaleIntercept` tags), as well as the default windowing stored in the DICOM file (`WindowCenter` and `WindowWidth`tags), and can be used to resize the resulting image. Color images are not affected by windowing.
        Tags: Instances

        Parameters
        ----------
        frame
            Index of the frame (starts at `0`)
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "height" (float): Height of the resized image
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
                "smooth" (bool): Whether to smooth image on resize
                "width" (float): Width of the resized image
                "window-center" (float): Windowing center
                "window-width" (float): Windowing width
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/frames/{frame}/rendered",
            params=params,
            headers=headers,
        )

    async def get_instances_id_header(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get DICOM meta-header

        Get the DICOM tags in the meta-header of the DICOM instance. By default, the `full` format is used, which combines hexadecimal tags with human-readable description.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the DICOM tags and their associated value
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/header",
            params=params,
        )

    async def get_instances_id_image_int16(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode an image (int16)

        Decode the first frame of the given DICOM instance. Pixels of grayscale images are truncated to the [-32768,32767] range. Negative values must be interpreted according to two's complement.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/image-int16",
            params=params,
            headers=headers,
        )

    async def get_instances_id_image_uint16(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode an image (uint16)

        Decode the first frame of the given DICOM instance. Pixels of grayscale images are truncated to the [0,65535] range.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/image-uint16",
            params=params,
            headers=headers,
        )

    async def get_instances_id_image_uint8(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode an image (uint8)

        Decode the first frame of the given DICOM instance. Pixels of grayscale images are truncated to the [0,255] range.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/image-uint8",
            params=params,
            headers=headers,
        )

    async def get_instances_id_labels(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List labels

        Get the labels that are associated with the given instance (new in Orthanc 1.12.0)
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the labels
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/labels",
        )

    async def delete_instances_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Remove label

        Remove a label associated with a instance
        Tags: Instances

        Parameters
        ----------
        label
            The label to be removed
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/instances/{id_}/labels/{label}",
        )

    async def get_instances_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Test label

        Test whether the instance is associated with the given label
        Tags: Instances

        Parameters
        ----------
        label
            The label of interest
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty string is returned in the case of presence, error 404 in the case of absence
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/labels/{label}",
        )

    async def put_instances_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Add label

        Associate a label with a instance
        Tags: Instances

        Parameters
        ----------
        label
            The label to be added
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/instances/{id_}/labels/{label}",
        )

    async def get_instances_id_matlab(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode frame for Matlab

        Decode the first frame of the given DICOM instance., and export this frame as a Octave/Matlab matrix to be imported with `eval()`: https://orthanc.uclouvain.be/book/faq/matlab.html
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Octave/Matlab matrix
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/matlab",
        )

    async def get_instances_id_metadata(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List metadata

        Get the list of metadata that are associated with the given instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If present, also retrieve the value of the individual metadata
                "numeric" (str): If present, use the numeric identifier of the metadata instead of its symbolic name

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the available metadata, or JSON associative array mapping metadata to their values (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/metadata",
            params=params,
        )

    async def delete_instances_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete metadata

        Delete some metadata associated with the given DICOM instance. This call will fail if trying to delete a system metadata (i.e. whose index is < 1024).
        Tags: Instances

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/instances/{id_}/metadata/{name}",
            headers=headers,
        )

    async def get_instances_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get metadata

        Get the value of a metadata that is associated with the given instance
        Tags: Instances

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the instance of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the metadata, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Value of the metadata
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/metadata/{name}",
            headers=headers,
        )

    async def put_instances_id_metadata_name(
        self,
        id_: str,
        name: str,
        data: RequestData = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set metadata

        Set the value of some metadata in the given DICOM instance. This call will fail if trying to modify a system metadata (i.e. whose index is < 1024).
        Tags: Instances

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the instance of interest
        data
            String value of the metadata
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, if this is not the first time this metadata is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/instances/{id_}/metadata/{name}",
            data=data,
            headers=headers,
        )

    async def post_instances_id_modify(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Modify instance

        Download a modified version of the DICOM instance whose Orthanc identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/anonymization.html#modification-of-a-single-instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        json
            Dictionary with the following keys:
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": Keep the original value of the specified tags, to be chosen among the `StudyInstanceUID`, `SeriesInstanceUID` and `SOPInstanceUID` tags. Avoid this feature as much as possible, as this breaks the DICOM model of the real world.
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of tags that must be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "RemovePrivateTags": Remove the private tags from the DICOM instances (defaults to `false`)
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The modified DICOM instance
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/instances/{id_}/modify",
            json=json,
        )

    async def get_instances_id_module(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get instance module

        Get the instance module of the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM instance
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/module",
            params=params,
        )

    async def get_instances_id_numpy(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode instance for numpy

        Decode the given DICOM instance, for use with numpy in Python. The numpy array has 4 dimensions: (frame, height, width, color channel).
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM resource of interest
        params
            Dictionary of optional parameters:
                "compress" (bool): Compress the file as `.npz`
                "rescale" (bool): On grayscale images, apply the rescaling and return floating-point values

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Numpy file: https://numpy.org/devdocs/reference/generated/numpy.lib.format.html
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/numpy",
            params=params,
        )

    async def get_instances_id_patient(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent patient

        Get detailed information about the parent patient of the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM patient
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/patient",
            params=params,
        )

    async def get_instances_id_pdf(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get embedded PDF

        Get the PDF file that is embedded in one DICOM instance. If the DICOM instance doesn't contain the `EncapsulatedDocument` tag or if the `MIMETypeOfEncapsulatedDocument` tag doesn't correspond to the PDF type, a `404` HTTP error is raised.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            PDF file
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/pdf",
        )

    async def get_instances_id_preview(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode an image (preview)

        Decode the first frame of the given DICOM instance. The full dynamic range of grayscale images is rescaled to the [0,255] range.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/preview",
            params=params,
            headers=headers,
        )

    async def post_instances_id_reconstruct(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Reconstruct tags & optionally files of instance

        Reconstruct the main DICOM tags in DB of the instance whose Orthanc identifier is provided in the URL. This is useful if child studies/series/instances have inconsistent values for higher-level tags, in order to force Orthanc to use the value from the resource of interest. Beware that this is a time-consuming operation, as all the children DICOM instances will be parsed again, and the Orthanc index will be updated accordingly.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        json
            Dictionary with the following keys:
              "LimitToThisLevelMainDicomTags": Only reconstruct this level MainDicomTags by re-reading them from a random child instance of the resource. This option is much faster than a full reconstruct and is useful e.g. if you have modified the 'ExtraMainDicomTags' at the Study level to optimize the speed of some C-Find. 'false' by default. (New in Orthanc 1.12.4)
              "ReconstructFiles": Also reconstruct the files of the resources (e.g: apply IngestTranscoding, StorageCompression). 'false' by default. (New in Orthanc 1.11.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/instances/{id_}/reconstruct",
            json=json,
        )

    async def get_instances_id_rendered(
        self,
        id_: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Render an image

        Render the first frame of the given DICOM instance. This function takes scaling into account (`RescaleSlope` and `RescaleIntercept` tags), as well as the default windowing stored in the DICOM file (`WindowCenter` and `WindowWidth`tags), and can be used to resize the resulting image. Color images are not affected by windowing.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "height" (float): Height of the resized image
                "quality" (float): Quality for JPEG images (between 1 and 100, defaults to 90)
                "returnUnsupportedImage" (bool): Returns an unsupported.png placeholder image if unable to provide the image instead of returning a 415 HTTP error (defaults to false)
                "smooth" (bool): Whether to smooth image on resize
                "width" (float): Width of the resized image
                "window-center" (float): Windowing center
                "window-width" (float): Windowing width
        headers
            Dictionary of optional headers:
                "Accept" (str): Format of the resulting image. Can be `image/png` (default), `image/jpeg` or `image/x-portable-arbitrarymap`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JPEG image
            PNG image
            PAM image (Portable Arbitrary Map)
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/rendered",
            params=params,
            headers=headers,
        )

    async def get_instances_id_series(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent series

        Get detailed information about the parent series of the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM series
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/series",
            params=params,
        )

    async def get_instances_id_simplified_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get human-readable tags

        Get the DICOM tags in human-readable format (same as the `/instances/{id}/tags?simplify` route)
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "whole" (bool): Whether to read the whole DICOM file from the storage area (new in Orthanc 1.12.4). If set to "false" (default value), the DICOM file is read until the pixel data tag (7fe0,0010) to optimize access to storage. Setting the option to "true" provides access to the DICOM tags stored after the pixel data tag.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the DICOM tags and their associated value
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/simplified-tags",
            params=params,
        )

    async def get_instances_id_statistics(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get instance statistics

        Get statistics about the given instance
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/statistics",
        )

    async def get_instances_id_study(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent study

        Get detailed information about the parent study of the DICOM instance whose Orthanc identifier is provided in the URL
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the instance of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM study
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/study",
            params=params,
        )

    async def get_instances_id_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get DICOM tags

        Get the DICOM tags in the specified format. By default, the `full` format is used, which combines hexadecimal tags with human-readable description.
        Tags: Instances

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM instance of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)
                "whole" (bool): Whether to read the whole DICOM file from the storage area (new in Orthanc 1.12.4). If set to "false" (default value), the DICOM file is read until the pixel data tag (7fe0,0010) to optimize access to storage. Setting the option to "true" provides access to the DICOM tags stored after the pixel data tag.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the DICOM tags and their associated value
        """
        return await self._get(
            route=f"{self.url}/instances/{id_}/tags",
            params=params,
        )

    async def get_jobs(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List jobs

        List all the available jobs
        Tags: Jobs

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual jobs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the jobs identifiers, or detailed information about the reported jobs (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/jobs",
            params=params,
        )

    async def delete_jobs_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete a job from history

        Delete the job from the jobs history.  Only a completed job can be deleted. If the job has not run or not completed yet, you must cancel it first. If the job has outputs, all outputs will be deleted as well.
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/jobs/{id_}",
        )

    async def get_jobs_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get job

        Retrieve detailed information about the job whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object detailing the job
        """
        return await self._get(
            route=f"{self.url}/jobs/{id_}",
        )

    async def post_jobs_id_cancel(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Cancel job

        Cancel the job whose identifier is provided in the URL. Check out the Orthanc Book for more information about the state machine applicable to jobs: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._post(
            route=f"{self.url}/jobs/{id_}/cancel",
        )

    async def post_jobs_id_pause(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Pause job

        Pause the job whose identifier is provided in the URL. Check out the Orthanc Book for more information about the state machine applicable to jobs: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._post(
            route=f"{self.url}/jobs/{id_}/pause",
        )

    async def post_jobs_id_resubmit(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Resubmit job

        Resubmit the job whose identifier is provided in the URL. Check out the Orthanc Book for more information about the state machine applicable to jobs: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._post(
            route=f"{self.url}/jobs/{id_}/resubmit",
        )

    async def post_jobs_id_resume(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Resume job

        Resume the job whose identifier is provided in the URL. Check out the Orthanc Book for more information about the state machine applicable to jobs: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
        Tags: Jobs

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._post(
            route=f"{self.url}/jobs/{id_}/resume",
        )

    async def delete_jobs_id_key(
        self,
        id_: str,
        key: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete a job output

        Delete the output produced by a job. As of Orthanc 1.12.1, only the jobs that generate a DICOMDIR media or a ZIP archive provide such an output (with `key` equals to `archive`).
        Tags: Jobs

        Parameters
        ----------
        key
            Name of the output of interest
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/jobs/{id_}/{key}",
        )

    async def get_jobs_id_key(
        self,
        id_: str,
        key: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get job output

        Retrieve some output produced by a job. As of Orthanc 1.8.2, only the jobs that generate a DICOMDIR media or a ZIP archive provide such an output (with `key` equals to `archive`).
        Tags: Jobs

        Parameters
        ----------
        key
            Name of the output of interest
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Content of the output of the job
        """
        return await self._get(
            route=f"{self.url}/jobs/{id_}/{key}",
        )

    async def get_modalities(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List DICOM modalities

        List all the DICOM modalities that are known to Orthanc. This corresponds either to the content of the `DicomModalities` configuration option, or to the information stored in the database if `DicomModalitiesInDatabase` is `true`.
        Tags: Networking

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual DICOM modalities

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the identifiers of the modalities, or detailed information about the modalities (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/modalities",
            params=params,
        )

    async def delete_modalities_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete DICOM modality

        Delete one DICOM modality. This change is permanent iff. `DicomModalitiesInDatabase` is `true`, otherwise it is lost at the next restart of Orthanc.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the DICOM modality of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/modalities/{id_}",
        )

    async def get_modalities_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on modality

        List the operations that are available for a DICOM modality.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the DICOM modality of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/modalities/{id_}",
        )

    async def put_modalities_id(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Update DICOM modality

        Define a new DICOM modality, or update an existing one. This change is permanent iff. `DicomModalitiesInDatabase` is `true`, otherwise it is lost at the next restart of Orthanc.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the new/updated DICOM modality
        json
            Dictionary with the following keys:
              "AET": AET of the remote DICOM modality
              "AllowEcho": Whether to accept C-ECHO SCU commands issued by the remote modality
              "AllowFind": Whether to accept C-FIND SCU commands issued by the remote modality
              "AllowFindWorklist": Whether to accept C-FIND SCU commands for worklists issued by the remote modality
              "AllowGet": Whether to accept C-GET SCU commands issued by the remote modality
              "AllowMove": Whether to accept C-MOVE SCU commands issued by the remote modality
              "AllowStorageCommitment": Whether to accept storage commitment requests issued by the remote modality
              "AllowStore": Whether to accept C-STORE SCU commands issued by the remote modality
              "AllowTranscoding": Whether to allow transcoding for operations initiated by this modality. This option applies to Orthanc C-GET SCP and to Orthanc C-STORE SCU. It only has an effect if the global option `EnableTranscoding` is set to `true`.
              "Host": Host address of the remote DICOM modality (typically, an IP address)
              "LocalAet": Whether to override the default DicomAet in the SCU connection initiated by Orthanc to this modality
              "Manufacturer": Manufacturer of the remote DICOM modality (check configuration option `DicomModalities` for possible values
              "Port": TCP port of the remote DICOM modality
              "Timeout": Whether to override the default DicomScuTimeout in the SCU connection initiated by Orthanc to this modality
              "UseDicomTls": Whether to use DICOM TLS in the SCU connection initiated by Orthanc (new in Orthanc 1.9.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._put(
            route=f"{self.url}/modalities/{id_}",
            json=json,
        )

    async def get_modalities_id_configuration(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get modality configuration

        Get detailed information about the configuration of some DICOM modality
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Configuration of the modality
        """
        return await self._get(
            route=f"{self.url}/modalities/{id_}/configuration",
        )

    async def post_modalities_id_echo(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-ECHO SCU

        Trigger C-ECHO SCU command against the DICOM modality whose identifier is provided in URL: https://orthanc.uclouvain.be/book/users/rest.html#performing-c-echo
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "CheckFind": Issue a dummy C-FIND command after the C-GET SCU, in order to check whether the remote modality knows about Orthanc. This field defaults to the value of the `DicomEchoChecksFind` configuration option. New in Orthanc 1.8.1.
              "Timeout": Timeout for the C-ECHO command, in seconds


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/echo",
            json=json,
        )

    async def post_modalities_id_find(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Hierarchical C-FIND SCU

        Trigger a sequence of C-FIND SCU commands against the DICOM modality whose identifier is provided in URL, in order to discover a hierarchy of matching patients/studies/series. Deprecated in favor of `/modalities/{id}/query`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching patients, embedding the matching studies, then the matching series.
        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find",
            json=json,
        )

    async def post_modalities_id_find_instance(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) C-FIND SCU for instances

        Trigger C-FIND SCU command against the DICOM modality whose identifier is provided in URL, in order to find an instance. Deprecated in favor of `/modalities/{id}/query`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching instances
        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find-instance",
            json=json,
        )

    async def post_modalities_id_find_patient(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) C-FIND SCU for patients

        Trigger C-FIND SCU command against the DICOM modality whose identifier is provided in URL, in order to find a patient. Deprecated in favor of `/modalities/{id}/query`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching patients
        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find-patient",
            json=json,
        )

    async def post_modalities_id_find_series(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) C-FIND SCU for series

        Trigger C-FIND SCU command against the DICOM modality whose identifier is provided in URL, in order to find a series. Deprecated in favor of `/modalities/{id}/query`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching series
        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find-series",
            json=json,
        )

    async def post_modalities_id_find_study(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) C-FIND SCU for studies

        Trigger C-FIND SCU command against the DICOM modality whose identifier is provided in URL, in order to find a study. Deprecated in favor of `/modalities/{id}/query`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching studies
        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find-study",
            json=json,
        )

    async def post_modalities_id_find_worklist(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) C-FIND SCU for worklist

        Trigger C-FIND SCU command against the remote worklists of the DICOM modality whose identifier is provided in URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Short": If set to `true`, report the DICOM tags in hexadecimal format


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array describing the DICOM tags of the matching worklists
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/find-worklist",
            json=json,
        )

    async def post_modalities_id_get(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-GET SCU

        Start a C-GET SCU command as a job, in order to retrieve DICOM resources from a remote DICOM modality whose identifier is provided in the URL:
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Level": Level of the query (`Patient`, `Study`, `Series` or `Instance`)
              "LocalAet": Local AET that is used for this commands, defaults to `DicomAet` configuration option. Ignored if `DicomModalities` already sets `LocalAet` for this modality.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": List of queries identifying all the DICOM resources to be sent.  Usage of wildcards is prohibited and the query shall only contain DICOM ID tags.  Additionally, you may provide SOPClassesInStudy to limit the scope of the DICOM negotiation to certain SOPClassUID or to present uncommon SOPClassUID during the DICOM negotation.  By default, Orhanc will propose the most 120 common SOPClassUIDs.
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Timeout": Timeout for the C-GET command, in seconds


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/get",
            json=json,
        )

    async def post_modalities_id_move(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-MOVE SCU

        Start a C-MOVE SCU command as a job, in order to drive the execution of a sequence of C-STORE commands by some remote DICOM modality whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/rest.html#performing-c-move
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Level": Level of the query (`Patient`, `Study`, `Series` or `Instance`)
              "LocalAet": Local AET that is used for this commands, defaults to `DicomAet` configuration option. Ignored if `DicomModalities` already sets `LocalAet` for this modality.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": List of queries identifying all the DICOM resources to be sent
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "TargetAet": Target AET that will be used by the remote DICOM modality as a target for its C-STORE SCU commands, defaults to `DicomAet` configuration option in order to do a simple query/retrieve
              "Timeout": Timeout for the C-MOVE command, in seconds


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/move",
            json=json,
        )

    async def post_modalities_id_query(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-FIND SCU

        Trigger C-FIND SCU command against the DICOM modality whose identifier is provided in URL: https://orthanc.uclouvain.be/book/users/rest.html#performing-query-retrieve-c-find-and-find-with-rest
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Level": Level of the query (`Patient`, `Study`, `Series` or `Instance`)
              "LocalAet": Local AET that is used for this commands, defaults to `DicomAet` configuration option. Ignored if `DicomModalities` already sets `LocalAet` for this modality.
              "Normalize": Whether to normalize the query, i.e. whether to wipe out from the query, the DICOM tags that are not applicable for the query-retrieve level of interest
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Timeout": Timeout for the C-FIND command and subsequent C-MOVE retrievals, in seconds (new in Orthanc 1.9.1)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/query",
            json=json,
        )

    async def post_modalities_id_storage_commitment(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger storage commitment request

        Trigger a storage commitment request to some remote DICOM modality whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/storage-commitment.html#storage-commitment-scu
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "DicomInstances": List of DICOM resources that are not necessarily stored within Orthanc, but that must be checked by storage commitment. This is a list of JSON objects that must contain the `SOPClassUID` and `SOPInstanceUID` fields.
              "Resources": List of the Orthanc identifiers of the DICOM resources to be checked by storage commitment
              "Timeout": Timeout for the storage commitment command (new in Orthanc 1.9.1)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/storage-commitment",
            json=json,
        )

    async def post_modalities_id_store(
        self,
        id_: str,
        data: RequestData = None,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-STORE SCU

        Start a C-STORE SCU command as a job, in order to send DICOM resources stored locally to some remote DICOM modality whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/rest.html#rest-store-scu
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "CalledAet": Called AET that is used for this commands, defaults to `AET` configuration option. Allows you to overwrite the destination AET for a specific operation.
              "Host": Host that is used for this commands, defaults to `Host` configuration option. Allows you to overwrite the destination host for a specific operation.
              "LocalAet": Local AET that is used for this commands, defaults to `DicomAet` configuration option. Ignored if `DicomModalities` already sets `LocalAet` for this modality.
              "MoveOriginatorAet": Move originator AET that is used for this commands, in order to fake a C-MOVE SCU
              "MoveOriginatorID": Move originator ID that is used for this commands, in order to fake a C-MOVE SCU
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Port": Port that is used for this command, defaults to `Port` configuration option. Allows you to overwrite the destination port for a specific operation.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": List of the Orthanc identifiers of all the DICOM resources to be sent
              "StorageCommitment": Whether to chain C-STORE with DICOM storage commitment to validate the success of the transmission: https://orthanc.uclouvain.be/book/users/storage-commitment.html#chaining-c-store-with-storage-commitment
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Timeout": Timeout for the C-STORE command, in seconds

        data
            The Orthanc identifier of one resource to be sent

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/modalities/{id_}/store",
            data=data,
            json=json,
        )

    async def post_modalities_id_store_straight(
        self,
        id_: str,
        content: RequestContent = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Straight C-STORE SCU

        Synchronously send the DICOM instance in the POST body to the remote DICOM modality whose identifier is provided in URL, without having to first store it locally within Orthanc. This is an alternative to command-line tools such as `storescu` from DCMTK or dcm4che.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        content
                - (Content-Type: "application/dicom") DICOM instance to be sent

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._post(
            route=f"{self.url}/modalities/{id_}/store-straight",
            content=content,
        )

    async def get_patients(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List the available patients

        List the Orthanc identifiers of all the available DICOM patients
        Tags: Patients

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual resources, not only their Orthanc identifiers
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "limit" (float): Limit the number of results
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "response-content" (str): Defines the content of response for each returned resource.  Allowed values are `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`, `Attachments`.  If not specified, Orthanc will return `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`.e.g: 'response-content=MainDicomTags;Children (new in Orthanc 1.12.5 - overrides `expand`)
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "since" (float): Show only the resources since the provided index

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the Orthanc identifiers, or detailed information about the reported patients (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/patients",
            params=params,
        )

    async def delete_patients_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete some patient

        Delete the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/patients/{id_}",
        )

    async def get_patients_id(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get information about some patient

        Get detailed information about the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM patient
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}",
            params=params,
        )

    async def post_patients_id_anonymize(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Anonymize patient

        Start a job that will anonymize all the DICOM instances within the patient whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new patient, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#anonymization-of-patients-studies-or-series
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "DicomVersion": Version of the DICOM standard to be used for anonymization. Check out configuration option `DeidentifyLogsDicomVersion` for possible values.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": List of DICOM tags whose value must not be destroyed by the anonymization. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepPrivateTags": Keep the private tags from the DICOM instances (defaults to `false`)
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of additional tags to be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/patients/{id_}/anonymize",
            json=json,
        )

    async def get_patients_id_archive(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Synchronously create a ZIP archive containing the DICOM patient whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/archive",
            params=params,
        )

    async def post_patients_id_archive(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Create a ZIP archive containing the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/patients/{id_}/archive",
            json=json,
        )

    async def get_patients_id_attachments(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List attachments

        Get the list of attachments that are associated with the given patient
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "full" (str): If present, retrieve the attachments list and their numerical ids

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the attachments
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments",
            params=params,
        )

    async def delete_patients_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete attachment

        Delete an attachment associated with the given DICOM patient. This call will fail if trying to delete a system attachment (i.e. whose index is < 1024).
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/patients/{id_}/attachments/{name}",
            headers=headers,
        )

    async def get_patients_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on attachments

        Get the list of the operations that are available for attachments associated with the given patient
        Tags: Other

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}",
            headers=headers,
        )

    async def put_patients_id_attachments_name(
        self,
        id_: str,
        name: str,
        content: RequestContent = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set attachment

        Attach a file to the given DICOM patient. This call will fail if trying to modify a system attachment (i.e. whose index is < 1024).
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        content
                - (Content-Type: "application/octet-stream") Binary data containing the attachment
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, if this is not the first time this attachment is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._put(
            route=f"{self.url}/patients/{id_}/attachments/{name}",
            content=content,
            headers=headers,
        )

    async def post_patients_id_attachments_name_compress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Compress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/patients/{id_}/attachments/{name}/compress",
        )

    async def get_patients_id_attachments_name_compressed_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment (no decompression)

        Get the (binary) content of one attachment associated with the given patient. The attachment will not be decompressed if `StorageCompression` is `true`.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/compressed-data",
            headers=headers,
        )

    async def get_patients_id_attachments_name_compressed_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment on disk

        Get the MD5 hash of one attachment associated with the given patient, as stored on the disk. This is different from `.../md5` iff `EnableStorage` is `true`.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/compressed-md5",
            headers=headers,
        )

    async def get_patients_id_attachments_name_compressed_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment on disk

        Get the size of one attachment associated with the given patient, as stored on the disk. This is different from `.../size` iff `EnableStorage` is `true`.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/compressed-size",
            headers=headers,
        )

    async def get_patients_id_attachments_name_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment

        Get the (binary) content of one attachment associated with the given patient
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/data",
            headers=headers,
        )

    async def get_patients_id_attachments_name_info(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get info about the attachment

        Get all the information about the attachment associated with the given patient
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the information about the attachment
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/info",
            headers=headers,
        )

    async def get_patients_id_attachments_name_is_compressed(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is attachment compressed?

        Test whether the attachment has been stored as a compressed file on the disk.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `0` if the attachment was stored uncompressed, `1` if it was compressed
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/is-compressed",
            headers=headers,
        )

    async def get_patients_id_attachments_name_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment

        Get the MD5 hash of one attachment associated with the given patient
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/md5",
            headers=headers,
        )

    async def get_patients_id_attachments_name_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment

        Get the size of one attachment associated with the given patient
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/attachments/{name}/size",
            headers=headers,
        )

    async def post_patients_id_attachments_name_uncompress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Uncompress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/patients/{id_}/attachments/{name}/uncompress",
        )

    async def post_patients_id_attachments_name_verify_md5(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Verify attachment

        Verify that the attachment is not corrupted, by validating its MD5 hash
        Tags: Patients

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            On success, a valid JSON object is returned
        """
        return await self._post(
            route=f"{self.url}/patients/{id_}/attachments/{name}/verify-md5",
        )

    async def get_patients_id_instances(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child instances

        Get detailed information about the child instances of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child instances
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM instances
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/instances",
            params=params,
        )

    async def get_patients_id_instances_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get tags of instances

        Get the tags of all the child instances of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object associating the Orthanc identifiers of the instances, with the values of their DICOM tags
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/instances-tags",
            params=params,
        )

    async def get_patients_id_labels(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List labels

        Get the labels that are associated with the given patient (new in Orthanc 1.12.0)
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the labels
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/labels",
        )

    async def delete_patients_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Remove label

        Remove a label associated with a patient
        Tags: Patients

        Parameters
        ----------
        label
            The label to be removed
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/patients/{id_}/labels/{label}",
        )

    async def get_patients_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Test label

        Test whether the patient is associated with the given label
        Tags: Patients

        Parameters
        ----------
        label
            The label of interest
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty string is returned in the case of presence, error 404 in the case of absence
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/labels/{label}",
        )

    async def put_patients_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Add label

        Associate a label with a patient
        Tags: Patients

        Parameters
        ----------
        label
            The label to be added
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/patients/{id_}/labels/{label}",
        )

    async def get_patients_id_media(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Synchronously create a DICOMDIR media containing the DICOM patient whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "extended" (str): If present, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/media",
            params=params,
        )

    async def post_patients_id_media(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Extended": If `true`, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*. Default value is `false`.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/patients/{id_}/media",
            json=json,
        )

    async def get_patients_id_metadata(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List metadata

        Get the list of metadata that are associated with the given patient
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If present, also retrieve the value of the individual metadata
                "numeric" (str): If present, use the numeric identifier of the metadata instead of its symbolic name

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the available metadata, or JSON associative array mapping metadata to their values (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/metadata",
            params=params,
        )

    async def delete_patients_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete metadata

        Delete some metadata associated with the given DICOM patient. This call will fail if trying to delete a system metadata (i.e. whose index is < 1024).
        Tags: Patients

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/patients/{id_}/metadata/{name}",
            headers=headers,
        )

    async def get_patients_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get metadata

        Get the value of a metadata that is associated with the given patient
        Tags: Patients

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the patient of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the metadata, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Value of the metadata
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/metadata/{name}",
            headers=headers,
        )

    async def put_patients_id_metadata_name(
        self,
        id_: str,
        name: str,
        data: RequestData = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set metadata

        Set the value of some metadata in the given DICOM patient. This call will fail if trying to modify a system metadata (i.e. whose index is < 1024).
        Tags: Patients

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the patient of interest
        data
            String value of the metadata
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, if this is not the first time this metadata is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/patients/{id_}/metadata/{name}",
            data=data,
            headers=headers,
        )

    async def post_patients_id_modify(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Modify patient

        Start a job that will modify all the DICOM instances within the patient whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new patient, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#modification-of-studies-or-series
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": Keep the original value of the specified tags, to be chosen among the `StudyInstanceUID`, `SeriesInstanceUID` and `SOPInstanceUID` tags. Avoid this feature as much as possible, as this breaks the DICOM model of the real world.
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of tags that must be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "RemovePrivateTags": Remove the private tags from the DICOM instances (defaults to `false`)
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/patients/{id_}/modify",
            json=json,
        )

    async def get_patients_id_module(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get patient module

        Get the patient module of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM patient
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/module",
            params=params,
        )

    async def get_patients_id_protected(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is the patient protected against recycling?

        Is the patient protected against recycling?
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `1` if protected, `0` if not protected
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/protected",
        )

    async def put_patients_id_protected(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Protect/Unprotect a patient against recycling

        Protects a patient by sending `1` or `true` in the payload request. Unprotects a patient by sending `0` or `false` in the payload requests. More info: https://orthanc.uclouvain.be/book/faq/features.html#recycling-protection
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/patients/{id_}/protected",
        )

    async def post_patients_id_reconstruct(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Reconstruct tags & optionally files of patient

        Reconstruct the main DICOM tags in DB of the patient whose Orthanc identifier is provided in the URL. This is useful if child studies/series/instances have inconsistent values for higher-level tags, in order to force Orthanc to use the value from the resource of interest. Beware that this is a time-consuming operation, as all the children DICOM instances will be parsed again, and the Orthanc index will be updated accordingly.
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        json
            Dictionary with the following keys:
              "LimitToThisLevelMainDicomTags": Only reconstruct this level MainDicomTags by re-reading them from a random child instance of the resource. This option is much faster than a full reconstruct and is useful e.g. if you have modified the 'ExtraMainDicomTags' at the Study level to optimize the speed of some C-Find. 'false' by default. (New in Orthanc 1.12.4)
              "ReconstructFiles": Also reconstruct the files of the resources (e.g: apply IngestTranscoding, StorageCompression). 'false' by default. (New in Orthanc 1.11.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/patients/{id_}/reconstruct",
            json=json,
        )

    async def get_patients_id_series(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child series

        Get detailed information about the child series of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child series
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM series
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/series",
            params=params,
        )

    async def get_patients_id_shared_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get shared tags

        Extract the DICOM tags whose value is constant across all the child instances of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the values of the DICOM tags
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/shared-tags",
            params=params,
        )

    async def get_patients_id_statistics(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get patient statistics

        Get statistics about the given patient
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/statistics",
        )

    async def get_patients_id_studies(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child studies

        Get detailed information about the child studies of the DICOM patient whose Orthanc identifier is provided in the URL
        Tags: Patients

        Parameters
        ----------
        id_
            Orthanc identifier of the patient of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child studies
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM studies
        """
        return await self._get(
            route=f"{self.url}/patients/{id_}/studies",
            params=params,
        )

    async def get_peers(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List Orthanc peers

        List all the Orthanc peers that are known to Orthanc. This corresponds either to the content of the `OrthancPeers` configuration option, or to the information stored in the database if `OrthancPeersInDatabase` is `true`.
        Tags: Networking

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual Orthanc peers

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the identifiers of the peers, or detailed information about the peers (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/peers",
            params=params,
        )

    async def delete_peers_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete Orthanc peer

        Delete one Orthanc peer. This change is permanent iff. `OrthancPeersInDatabase` is `true`, otherwise it is lost at the next restart of Orthanc.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the Orthanc peer of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/peers/{id_}",
        )

    async def get_peers_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on peer

        List the operations that are available for an Orthanc peer.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the peer of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/peers/{id_}",
        )

    async def put_peers_id(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Update Orthanc peer

        Define a new Orthanc peer, or update an existing one. This change is permanent iff. `OrthancPeersInDatabase` is `true`, otherwise it is lost at the next restart of Orthanc.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the new/updated Orthanc peer
        json
            Dictionary with the following keys:
              "CertificateFile": SSL certificate for the HTTPS connections
              "CertificateKeyFile": Key file for the SSL certificate for the HTTPS connections
              "CertificateKeyPassword": Key password for the SSL certificate for the HTTPS connections
              "HttpHeaders": HTTP headers to be used for the connections to the remote peer
              "Password": Password for the credentials
              "URL": URL of the root of the REST API of the remote Orthanc peer, for instance `http://localhost:8042/`
              "Username": Username for the credentials


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._put(
            route=f"{self.url}/peers/{id_}",
            json=json,
        )

    async def get_peers_id_configuration(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get peer configuration

        Get detailed information about the configuration of some Orthanc peer
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the peer of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Configuration of the peer
        """
        return await self._get(
            route=f"{self.url}/peers/{id_}/configuration",
        )

    async def post_peers_id_store(
        self,
        id_: str,
        data: RequestData = None,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Send to Orthanc peer

        Send DICOM resources stored locally to some remote Orthanc peer whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/rest.html#sending-one-resource
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Compress": Whether to compress the DICOM instances using gzip before the actual sending
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": List of the Orthanc identifiers of all the DICOM resources to be sent
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode to the provided DICOM transfer syntax before the actual sending

        data
            The Orthanc identifier of one resource to be sent

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/peers/{id_}/store",
            data=data,
            json=json,
        )

    async def post_peers_id_store_straight(
        self,
        id_: str,
        content: RequestContent = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Straight store to peer

        Synchronously send the DICOM instance in the POST body to the Orthanc peer whose identifier is provided in URL, without having to first store it locally within Orthanc. This is an alternative to command-line tools such as `curl`.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the modality of interest
        content
                - (Content-Type: "application/dicom") DICOM instance to be sent

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._post(
            route=f"{self.url}/peers/{id_}/store-straight",
            content=content,
        )

    async def get_peers_id_system(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get peer system information

        Get system information about some Orthanc peer. This corresponds to doing a `GET` request against the `/system` URI of the remote peer. This route can be used to test connectivity.
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the peer of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            System information about the peer
        """
        return await self._get(
            route=f"{self.url}/peers/{id_}/system",
        )

    async def get_plugins(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List plugins

        List all the installed plugins
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the identifiers of the installed plugins
        """
        return await self._get(
            route=f"{self.url}/plugins",
        )

    async def get_plugins_explorer_js(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) JavaScript extensions to Orthanc Explorer

        Get the JavaScript extensions that are installed by all the plugins using the `OrthancPluginExtendOrthancExplorer()` function of the plugin SDK. This route is for internal use of Orthanc Explorer.
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The JavaScript extensions
        """
        return await self._get(
            route=f"{self.url}/plugins/explorer.js",
        )

    async def get_plugins_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get plugin

        Get system information about the plugin whose identifier is provided in the URL
        Tags: System

        Parameters
        ----------
        id_
            Identifier of the job of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing information about the plugin
        """
        return await self._get(
            route=f"{self.url}/plugins/{id_}",
        )

    async def get_queries(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List query/retrieve operations

        List the identifiers of all the query/retrieve operations on DICOM modalities, as initiated by calls to `/modalities/{id}/query`. The length of this list is bounded by the `QueryRetrieveSize` configuration option of Orthanc. https://orthanc.uclouvain.be/book/users/rest.html#performing-query-retrieve-c-find-and-find-with-rest
        Tags: Networking

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the identifiers
        """
        return await self._get(
            route=f"{self.url}/queries",
        )

    async def delete_queries_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete a query

        Delete the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/queries/{id_}",
        )

    async def get_queries_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on a query

        List the available operations for the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the list of operations
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}",
        )

    async def get_queries_id_answers(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List answers to a query

        List the indices of all the available answers resulting from a query/retrieve operation on some DICOM modality, whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual answers
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the indices of the answers, or detailed information about the reported answers (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/answers",
            params=params,
        )

    async def get_queries_id_answers_index(
        self,
        id_: str,
        index: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on an answer

        List the available operations on an answer associated with the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the list of operations
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/answers/{index}",
        )

    async def get_queries_id_answers_index_content(
        self,
        id_: str,
        index: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get one answer

        Get the content (DICOM tags) of one answer associated with the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the DICOM tags of the answer
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/answers/{index}/content",
            params=params,
        )

    async def post_queries_id_answers_index_query_instances(
        self,
        id_: str,
        index: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Query the child instances of an answer

        Issue a second DICOM C-FIND operation, in order to query the child instances associated with one answer to some query/retrieve operation whose identifiers are provided in the URL
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest
        json
            Dictionary with the following keys:
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Timeout": Timeout for the C-FIND command, in seconds (new in Orthanc 1.9.1)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/queries/{id_}/answers/{index}/query-instances",
            json=json,
        )

    async def post_queries_id_answers_index_query_series(
        self,
        id_: str,
        index: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Query the child series of an answer

        Issue a second DICOM C-FIND operation, in order to query the child series associated with one answer to some query/retrieve operation whose identifiers are provided in the URL
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest
        json
            Dictionary with the following keys:
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Timeout": Timeout for the C-FIND command, in seconds (new in Orthanc 1.9.1)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/queries/{id_}/answers/{index}/query-series",
            json=json,
        )

    async def post_queries_id_answers_index_query_studies(
        self,
        id_: str,
        index: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Query the child studies of an answer

        Issue a second DICOM C-FIND operation, in order to query the child studies associated with one answer to some query/retrieve operation whose identifiers are provided in the URL
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest
        json
            Dictionary with the following keys:
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Timeout": Timeout for the C-FIND command, in seconds (new in Orthanc 1.9.1)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/queries/{id_}/answers/{index}/query-studies",
            json=json,
        )

    async def post_queries_id_answers_index_retrieve(
        self,
        id_: str,
        index: str,
        data: RequestData = None,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Retrieve one answer with a C-MOVE or a C-GET SCU

        Start a C-MOVE or a C-GET SCU command as a job, in order to retrieve one answer associated with the query/retrieve operation whose identifiers are provided in the URL: https://orthanc.uclouvain.be/book/users/rest.html#performing-retrieve-c-move
        Tags: Networking

        Parameters
        ----------
        index
            Index of the answer
        id_
            Identifier of the query of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "RetrieveMethod": Force usage of C-MOVE or C-GET to retrieve the resource.  If note defined in the payload, the retrieve method is defined in the DicomDefaultRetrieveMethod configuration or in DicomModalities->..->RetrieveMethod
              "Simplify": If set to `true`, report the DICOM tags in human-readable format (using the symbolic name of the tags)
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "TargetAet": AET of the target modality. By default, the AET of Orthanc is used, as defined in the `DicomAet` configuration option.
              "Timeout": Timeout for the C-MOVE command, in seconds

        data
            AET of the target modality

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/queries/{id_}/answers/{index}/retrieve",
            data=data,
            json=json,
        )

    async def get_queries_id_level(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get level of original query

        Get the query level (value of the `QueryRetrieveLevel` tag) of the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The level
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/level",
        )

    async def get_queries_id_modality(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get modality of original query

        Get the identifier of the DICOM modality that was targeted by the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The identifier of the DICOM modality
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/modality",
        )

    async def get_queries_id_query(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get original query arguments

        Get the original DICOM filter associated with the query/retrieve operation whose identifier is provided in the URL
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Content of the original query
        """
        return await self._get(
            route=f"{self.url}/queries/{id_}/query",
            params=params,
        )

    async def post_queries_id_retrieve(
        self,
        id_: str,
        data: RequestData = None,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Retrieve all answers with C-MOVE SCU

        Start a C-MOVE SCU command as a job, in order to retrieve all the answers associated with the query/retrieve operation whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/rest.html#performing-retrieve-c-move
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the query of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "RetrieveMethod": Force usage of C-MOVE or C-GET to retrieve the resource.  If note defined in the payload, the retrieve method is defined in the DicomDefaultRetrieveMethod configuration or in DicomModalities->..->RetrieveMethod
              "Simplify": If set to `true`, report the DICOM tags in human-readable format (using the symbolic name of the tags)
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "TargetAet": AET of the target modality. By default, the AET of Orthanc is used, as defined in the `DicomAet` configuration option.
              "Timeout": Timeout for the C-MOVE command, in seconds

        data
            AET of the target modality

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/queries/{id_}/retrieve",
            data=data,
            json=json,
        )

    async def get_series(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List the available series

        List the Orthanc identifiers of all the available DICOM series
        Tags: Series

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual resources, not only their Orthanc identifiers
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "limit" (float): Limit the number of results
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "response-content" (str): Defines the content of response for each returned resource.  Allowed values are `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`, `Attachments`.  If not specified, Orthanc will return `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`.e.g: 'response-content=MainDicomTags;Children (new in Orthanc 1.12.5 - overrides `expand`)
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "since" (float): Show only the resources since the provided index

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the Orthanc identifiers, or detailed information about the reported series (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/series",
            params=params,
        )

    async def delete_series_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete some series

        Delete the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/series/{id_}",
        )

    async def get_series_id(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get information about some series

        Get detailed information about the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM series
        """
        return await self._get(
            route=f"{self.url}/series/{id_}",
            params=params,
        )

    async def post_series_id_anonymize(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Anonymize series

        Start a job that will anonymize all the DICOM instances within the series whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new series, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#anonymization-of-patients-studies-or-series
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "DicomVersion": Version of the DICOM standard to be used for anonymization. Check out configuration option `DeidentifyLogsDicomVersion` for possible values.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": List of DICOM tags whose value must not be destroyed by the anonymization. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepPrivateTags": Keep the private tags from the DICOM instances (defaults to `false`)
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of additional tags to be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/series/{id_}/anonymize",
            json=json,
        )

    async def get_series_id_archive(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Synchronously create a ZIP archive containing the DICOM series whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/archive",
            params=params,
        )

    async def post_series_id_archive(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Create a ZIP archive containing the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/series/{id_}/archive",
            json=json,
        )

    async def get_series_id_attachments(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List attachments

        Get the list of attachments that are associated with the given series
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "full" (str): If present, retrieve the attachments list and their numerical ids

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the attachments
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments",
            params=params,
        )

    async def delete_series_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete attachment

        Delete an attachment associated with the given DICOM series. This call will fail if trying to delete a system attachment (i.e. whose index is < 1024).
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/series/{id_}/attachments/{name}",
            headers=headers,
        )

    async def get_series_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on attachments

        Get the list of the operations that are available for attachments associated with the given series
        Tags: Other

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}",
            headers=headers,
        )

    async def put_series_id_attachments_name(
        self,
        id_: str,
        name: str,
        content: RequestContent = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set attachment

        Attach a file to the given DICOM series. This call will fail if trying to modify a system attachment (i.e. whose index is < 1024).
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        content
                - (Content-Type: "application/octet-stream") Binary data containing the attachment
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, if this is not the first time this attachment is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._put(
            route=f"{self.url}/series/{id_}/attachments/{name}",
            content=content,
            headers=headers,
        )

    async def post_series_id_attachments_name_compress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Compress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/series/{id_}/attachments/{name}/compress",
        )

    async def get_series_id_attachments_name_compressed_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment (no decompression)

        Get the (binary) content of one attachment associated with the given series. The attachment will not be decompressed if `StorageCompression` is `true`.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/compressed-data",
            headers=headers,
        )

    async def get_series_id_attachments_name_compressed_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment on disk

        Get the MD5 hash of one attachment associated with the given series, as stored on the disk. This is different from `.../md5` iff `EnableStorage` is `true`.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/compressed-md5",
            headers=headers,
        )

    async def get_series_id_attachments_name_compressed_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment on disk

        Get the size of one attachment associated with the given series, as stored on the disk. This is different from `.../size` iff `EnableStorage` is `true`.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/compressed-size",
            headers=headers,
        )

    async def get_series_id_attachments_name_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment

        Get the (binary) content of one attachment associated with the given series
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/data",
            headers=headers,
        )

    async def get_series_id_attachments_name_info(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get info about the attachment

        Get all the information about the attachment associated with the given series
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the information about the attachment
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/info",
            headers=headers,
        )

    async def get_series_id_attachments_name_is_compressed(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is attachment compressed?

        Test whether the attachment has been stored as a compressed file on the disk.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `0` if the attachment was stored uncompressed, `1` if it was compressed
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/is-compressed",
            headers=headers,
        )

    async def get_series_id_attachments_name_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment

        Get the MD5 hash of one attachment associated with the given series
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/md5",
            headers=headers,
        )

    async def get_series_id_attachments_name_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment

        Get the size of one attachment associated with the given series
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/attachments/{name}/size",
            headers=headers,
        )

    async def post_series_id_attachments_name_uncompress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Uncompress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/series/{id_}/attachments/{name}/uncompress",
        )

    async def post_series_id_attachments_name_verify_md5(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Verify attachment

        Verify that the attachment is not corrupted, by validating its MD5 hash
        Tags: Series

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            On success, a valid JSON object is returned
        """
        return await self._post(
            route=f"{self.url}/series/{id_}/attachments/{name}/verify-md5",
        )

    async def get_series_id_instances(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child instances

        Get detailed information about the child instances of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child instances
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM instances
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/instances",
            params=params,
        )

    async def get_series_id_instances_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get tags of instances

        Get the tags of all the child instances of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object associating the Orthanc identifiers of the instances, with the values of their DICOM tags
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/instances-tags",
            params=params,
        )

    async def get_series_id_labels(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List labels

        Get the labels that are associated with the given series (new in Orthanc 1.12.0)
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the labels
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/labels",
        )

    async def delete_series_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Remove label

        Remove a label associated with a series
        Tags: Series

        Parameters
        ----------
        label
            The label to be removed
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/series/{id_}/labels/{label}",
        )

    async def get_series_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Test label

        Test whether the series is associated with the given label
        Tags: Series

        Parameters
        ----------
        label
            The label of interest
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty string is returned in the case of presence, error 404 in the case of absence
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/labels/{label}",
        )

    async def put_series_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Add label

        Associate a label with a series
        Tags: Series

        Parameters
        ----------
        label
            The label to be added
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/series/{id_}/labels/{label}",
        )

    async def get_series_id_media(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Synchronously create a DICOMDIR media containing the DICOM series whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "extended" (str): If present, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/media",
            params=params,
        )

    async def post_series_id_media(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Extended": If `true`, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*. Default value is `false`.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/series/{id_}/media",
            json=json,
        )

    async def get_series_id_metadata(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List metadata

        Get the list of metadata that are associated with the given series
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If present, also retrieve the value of the individual metadata
                "numeric" (str): If present, use the numeric identifier of the metadata instead of its symbolic name

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the available metadata, or JSON associative array mapping metadata to their values (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/metadata",
            params=params,
        )

    async def delete_series_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete metadata

        Delete some metadata associated with the given DICOM series. This call will fail if trying to delete a system metadata (i.e. whose index is < 1024).
        Tags: Series

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/series/{id_}/metadata/{name}",
            headers=headers,
        )

    async def get_series_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get metadata

        Get the value of a metadata that is associated with the given series
        Tags: Series

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the series of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the metadata, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Value of the metadata
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/metadata/{name}",
            headers=headers,
        )

    async def put_series_id_metadata_name(
        self,
        id_: str,
        name: str,
        data: RequestData = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set metadata

        Set the value of some metadata in the given DICOM series. This call will fail if trying to modify a system metadata (i.e. whose index is < 1024).
        Tags: Series

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the series of interest
        data
            String value of the metadata
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, if this is not the first time this metadata is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/series/{id_}/metadata/{name}",
            data=data,
            headers=headers,
        )

    async def post_series_id_modify(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Modify series

        Start a job that will modify all the DICOM instances within the series whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new series, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#modification-of-studies-or-series
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": Keep the original value of the specified tags, to be chosen among the `StudyInstanceUID`, `SeriesInstanceUID` and `SOPInstanceUID` tags. Avoid this feature as much as possible, as this breaks the DICOM model of the real world.
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of tags that must be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "RemovePrivateTags": Remove the private tags from the DICOM instances (defaults to `false`)
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/series/{id_}/modify",
            json=json,
        )

    async def get_series_id_module(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get series module

        Get the series module of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM series
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/module",
            params=params,
        )

    async def get_series_id_numpy(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Decode series for numpy

        Decode the given DICOM series, for use with numpy in Python. The numpy array has 4 dimensions: (frame, height, width, color channel).
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the DICOM resource of interest
        params
            Dictionary of optional parameters:
                "compress" (bool): Compress the file as `.npz`
                "rescale" (bool): On grayscale images, apply the rescaling and return floating-point values

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Numpy file: https://numpy.org/devdocs/reference/generated/numpy.lib.format.html
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/numpy",
            params=params,
        )

    async def get_series_id_ordered_slices(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Order the slices

        Sort the instances and frames (slices) of the DICOM series whose Orthanc identifier is provided in the URL. This URI is essentially used by the Orthanc Web viewer and by the Osimis Web viewer.
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        warnings.warn("This method is deprecated.", DeprecationWarning, stacklevel=2)
        return await self._get(
            route=f"{self.url}/series/{id_}/ordered-slices",
        )

    async def get_series_id_patient(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent patient

        Get detailed information about the parent patient of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM patient
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/patient",
            params=params,
        )

    async def post_series_id_reconstruct(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Reconstruct tags & optionally files of series

        Reconstruct the main DICOM tags in DB of the series whose Orthanc identifier is provided in the URL. This is useful if child studies/series/instances have inconsistent values for higher-level tags, in order to force Orthanc to use the value from the resource of interest. Beware that this is a time-consuming operation, as all the children DICOM instances will be parsed again, and the Orthanc index will be updated accordingly.
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        json
            Dictionary with the following keys:
              "LimitToThisLevelMainDicomTags": Only reconstruct this level MainDicomTags by re-reading them from a random child instance of the resource. This option is much faster than a full reconstruct and is useful e.g. if you have modified the 'ExtraMainDicomTags' at the Study level to optimize the speed of some C-Find. 'false' by default. (New in Orthanc 1.12.4)
              "ReconstructFiles": Also reconstruct the files of the resources (e.g: apply IngestTranscoding, StorageCompression). 'false' by default. (New in Orthanc 1.11.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/series/{id_}/reconstruct",
            json=json,
        )

    async def get_series_id_shared_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get shared tags

        Extract the DICOM tags whose value is constant across all the child instances of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the values of the DICOM tags
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/shared-tags",
            params=params,
        )

    async def get_series_id_statistics(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get series statistics

        Get statistics about the given series
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/series/{id_}/statistics",
        )

    async def get_series_id_study(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent study

        Get detailed information about the parent study of the DICOM series whose Orthanc identifier is provided in the URL
        Tags: Series

        Parameters
        ----------
        id_
            Orthanc identifier of the series of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM study
        """
        return await self._get(
            route=f"{self.url}/series/{id_}/study",
            params=params,
        )

    async def get_statistics(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get database statistics

        Get statistics related to the database of Orthanc
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/statistics",
        )

    async def get_storage_commitment_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get storage commitment report

        Get the storage commitment report whose identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/storage-commitment.html#storage-commitment-scu
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the storage commitment report

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/storage-commitment/{id_}",
        )

    async def post_storage_commitment_id_remove(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Remove after storage commitment

        Remove out of Orthanc, the DICOM instances that have been reported to have been properly received the storage commitment report whose identifier is provided in the URL. This is only possible if the `Status` of the storage commitment report is `Success`. https://orthanc.uclouvain.be/book/users/storage-commitment.html#removing-the-instances
        Tags: Networking

        Parameters
        ----------
        id_
            Identifier of the storage commitment report

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/storage-commitment/{id_}/remove",
        )

    async def get_studies(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List the available studies

        List the Orthanc identifiers of all the available DICOM studies
        Tags: Studies

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "expand" (str): If present, retrieve detailed information about the individual resources, not only their Orthanc identifiers
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "limit" (float): Limit the number of results
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "response-content" (str): Defines the content of response for each returned resource.  Allowed values are `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`, `Attachments`.  If not specified, Orthanc will return `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`.e.g: 'response-content=MainDicomTags;Children (new in Orthanc 1.12.5 - overrides `expand`)
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "since" (float): Show only the resources since the provided index

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the Orthanc identifiers, or detailed information about the reported studies (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/studies",
            params=params,
        )

    async def delete_studies_id(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete some study

        Delete the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/studies/{id_}",
        )

    async def get_studies_id(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get information about some study

        Get detailed information about the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM study
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}",
            params=params,
        )

    async def post_studies_id_anonymize(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Anonymize study

        Start a job that will anonymize all the DICOM instances within the study whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new study, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#anonymization-of-patients-studies-or-series
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "DicomVersion": Version of the DICOM standard to be used for anonymization. Check out configuration option `DeidentifyLogsDicomVersion` for possible values.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": List of DICOM tags whose value must not be destroyed by the anonymization. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepPrivateTags": Keep the private tags from the DICOM instances (defaults to `false`)
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of additional tags to be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/anonymize",
            json=json,
        )

    async def get_studies_id_archive(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Synchronously create a ZIP archive containing the DICOM study whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/archive",
            params=params,
        )

    async def post_studies_id_archive(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Create a ZIP archive containing the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/archive",
            json=json,
        )

    async def get_studies_id_attachments(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List attachments

        Get the list of attachments that are associated with the given study
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "full" (str): If present, retrieve the attachments list and their numerical ids

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the attachments
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments",
            params=params,
        )

    async def delete_studies_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete attachment

        Delete an attachment associated with the given DICOM study. This call will fail if trying to delete a system attachment (i.e. whose index is < 1024).
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/studies/{id_}/attachments/{name}",
            headers=headers,
        )

    async def get_studies_id_attachments_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations on attachments

        Get the list of the operations that are available for attachments associated with the given study
        Tags: Other

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}",
            headers=headers,
        )

    async def put_studies_id_attachments_name(
        self,
        id_: str,
        name: str,
        content: RequestContent = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set attachment

        Attach a file to the given DICOM study. This call will fail if trying to modify a system attachment (i.e. whose index is < 1024).
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        content
                - (Content-Type: "application/octet-stream") Binary data containing the attachment
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the attachment, if this is not the first time this attachment is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty JSON object in the case of a success
        """
        return await self._put(
            route=f"{self.url}/studies/{id_}/attachments/{name}",
            content=content,
            headers=headers,
        )

    async def post_studies_id_attachments_name_compress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Compress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/studies/{id_}/attachments/{name}/compress",
        )

    async def get_studies_id_attachments_name_compressed_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment (no decompression)

        Get the (binary) content of one attachment associated with the given study. The attachment will not be decompressed if `StorageCompression` is `true`.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/compressed-data",
            headers=headers,
        )

    async def get_studies_id_attachments_name_compressed_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment on disk

        Get the MD5 hash of one attachment associated with the given study, as stored on the disk. This is different from `.../md5` iff `EnableStorage` is `true`.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/compressed-md5",
            headers=headers,
        )

    async def get_studies_id_attachments_name_compressed_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment on disk

        Get the size of one attachment associated with the given study, as stored on the disk. This is different from `.../size` iff `EnableStorage` is `true`.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment, as stored on the disk
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/compressed-size",
            headers=headers,
        )

    async def get_studies_id_attachments_name_data(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get attachment

        Get the (binary) content of one attachment associated with the given study
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "Content-Range" (str): Optional content range to access part of the attachment (new in Orthanc 1.12.5)
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The attachment
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/data",
            headers=headers,
        )

    async def get_studies_id_attachments_name_info(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get info about the attachment

        Get all the information about the attachment associated with the given study
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the information about the attachment
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/info",
            headers=headers,
        )

    async def get_studies_id_attachments_name_is_compressed(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is attachment compressed?

        Test whether the attachment has been stored as a compressed file on the disk.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `0` if the attachment was stored uncompressed, `1` if it was compressed
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/is-compressed",
            headers=headers,
        )

    async def get_studies_id_attachments_name_md5(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get MD5 of attachment

        Get the MD5 hash of one attachment associated with the given study
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The MD5 of the attachment
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/md5",
            headers=headers,
        )

    async def get_studies_id_attachments_name_size(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get size of attachment

        Get the size of one attachment associated with the given study
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the attachment, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The size of the attachment
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/attachments/{name}/size",
            headers=headers,
        )

    async def post_studies_id_attachments_name_uncompress(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Uncompress attachment

        Change the compression scheme that is used to store an attachment.
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/studies/{id_}/attachments/{name}/uncompress",
        )

    async def post_studies_id_attachments_name_verify_md5(
        self,
        id_: str,
        name: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Verify attachment

        Verify that the attachment is not corrupted, by validating its MD5 hash
        Tags: Studies

        Parameters
        ----------
        name
            The name of the attachment, or its index (cf. `UserContentType` configuration option)
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            On success, a valid JSON object is returned
        """
        return await self._post(
            route=f"{self.url}/studies/{id_}/attachments/{name}/verify-md5",
        )

    async def get_studies_id_instances(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child instances

        Get detailed information about the child instances of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child instances
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM instances
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/instances",
            params=params,
        )

    async def get_studies_id_instances_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get tags of instances

        Get the tags of all the child instances of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object associating the Orthanc identifiers of the instances, with the values of their DICOM tags
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/instances-tags",
            params=params,
        )

    async def get_studies_id_labels(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List labels

        Get the labels that are associated with the given study (new in Orthanc 1.12.0)
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the labels
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/labels",
        )

    async def delete_studies_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Remove label

        Remove a label associated with a study
        Tags: Studies

        Parameters
        ----------
        label
            The label to be removed
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/studies/{id_}/labels/{label}",
        )

    async def get_studies_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Test label

        Test whether the study is associated with the given label
        Tags: Studies

        Parameters
        ----------
        label
            The label of interest
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Empty string is returned in the case of presence, error 404 in the case of absence
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/labels/{label}",
        )

    async def put_studies_id_labels_label(
        self,
        id_: str,
        label: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Add label

        Associate a label with a study
        Tags: Studies

        Parameters
        ----------
        label
            The label to be added
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/studies/{id_}/labels/{label}",
        )

    async def get_studies_id_media(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Synchronously create a DICOMDIR media containing the DICOM study whose Orthanc identifier is provided in the URL. This flavor is synchronous, which might *not* be desirable to archive large amount of data, as it might lead to network timeouts. Prefer the asynchronous version using `POST` method.
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "extended" (str): If present, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*
                "filename" (str): Filename to set in the "Content-Disposition" HTTP header (including file extension)
                "transcode" (str): If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            ZIP file containing the archive
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/media",
            params=params,
        )

    async def post_studies_id_media(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Extended": If `true`, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*. Default value is `false`.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/media",
            json=json,
        )

    async def post_studies_id_merge(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Merge study

        Start a new job so as to move some DICOM resources into the DICOM study whose Orthanc identifier is provided in the URL: https://orthanc.uclouvain.be/book/users/anonymization.html#merging
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "KeepSource": If set to `true`, instructs Orthanc to keep a copy of the original resources in their source study. By default, the original resources are deleted from Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": The list of DICOM resources (studies, series, and/or instances) to be merged into the study of interest (mandatory option)
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/merge",
            json=json,
        )

    async def get_studies_id_metadata(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List metadata

        Get the list of metadata that are associated with the given study
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If present, also retrieve the value of the individual metadata
                "numeric" (str): If present, use the numeric identifier of the metadata instead of its symbolic name

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the names of the available metadata, or JSON associative array mapping metadata to their values (if `expand` argument is provided)
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/metadata",
            params=params,
        )

    async def delete_studies_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete metadata

        Delete some metadata associated with the given DICOM study. This call will fail if trying to delete a system metadata (i.e. whose index is < 1024).
        Tags: Studies

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, to check if its content has not changed and can be deleted. This header is mandatory if `CheckRevisions` option is `true`.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._delete(
            route=f"{self.url}/studies/{id_}/metadata/{name}",
            headers=headers,
        )

    async def get_studies_id_metadata_name(
        self,
        id_: str,
        name: str,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get metadata

        Get the value of a metadata that is associated with the given study
        Tags: Studies

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the study of interest
        headers
            Dictionary of optional headers:
                "If-None-Match" (str): Optional revision of the metadata, to check if its content has changed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Value of the metadata
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/metadata/{name}",
            headers=headers,
        )

    async def put_studies_id_metadata_name(
        self,
        id_: str,
        name: str,
        data: RequestData = None,
        headers: HeaderTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set metadata

        Set the value of some metadata in the given DICOM study. This call will fail if trying to modify a system metadata (i.e. whose index is < 1024).
        Tags: Studies

        Parameters
        ----------
        name
            The name of the metadata, or its index (cf. `UserMetadata` configuration option)
        id_
            Orthanc identifier of the study of interest
        data
            String value of the metadata
        headers
            Dictionary of optional headers:
                "If-Match" (str): Revision of the metadata, if this is not the first time this metadata is set.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/studies/{id_}/metadata/{name}",
            data=data,
            headers=headers,
        )

    async def post_studies_id_modify(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Modify study

        Start a job that will modify all the DICOM instances within the study whose identifier is provided in the URL. The modified DICOM instances will be stored into a brand new study, whose Orthanc identifiers will be returned by the job. https://orthanc.uclouvain.be/book/users/anonymization.html#modification-of-studies-or-series
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": Keep the original value of the specified tags, to be chosen among the `StudyInstanceUID`, `SeriesInstanceUID` and `SOPInstanceUID` tags. Avoid this feature as much as possible, as this breaks the DICOM model of the real world.
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of tags that must be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "RemovePrivateTags": Remove the private tags from the DICOM instances (defaults to `false`)
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/modify",
            json=json,
        )

    async def get_studies_id_module(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get study module

        Get the study module of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM study
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/module",
            params=params,
        )

    async def get_studies_id_module_patient(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get patient module of study

        Get the patient module of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "ignore-length" (List): Also include the DICOM tags that are provided in this list, even if their associated value is long
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the DICOM study
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/module-patient",
            params=params,
        )

    async def get_studies_id_patient(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get parent patient

        Get detailed information about the parent patient of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Information about the parent DICOM patient
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/patient",
            params=params,
        )

    async def post_studies_id_reconstruct(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Reconstruct tags & optionally files of study

        Reconstruct the main DICOM tags in DB of the study whose Orthanc identifier is provided in the URL. This is useful if child studies/series/instances have inconsistent values for higher-level tags, in order to force Orthanc to use the value from the resource of interest. Beware that this is a time-consuming operation, as all the children DICOM instances will be parsed again, and the Orthanc index will be updated accordingly.
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "LimitToThisLevelMainDicomTags": Only reconstruct this level MainDicomTags by re-reading them from a random child instance of the resource. This option is much faster than a full reconstruct and is useful e.g. if you have modified the 'ExtraMainDicomTags' at the Study level to optimize the speed of some C-Find. 'false' by default. (New in Orthanc 1.12.4)
              "ReconstructFiles": Also reconstruct the files of the resources (e.g: apply IngestTranscoding, StorageCompression). 'false' by default. (New in Orthanc 1.11.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/reconstruct",
            json=json,
        )

    async def get_studies_id_series(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get child series

        Get detailed information about the child series of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "expand" (str): If false or missing, only retrieve the list of child series
                "full" (bool): If present, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
                "requested-tags" (str): If present, list the DICOM Tags you want to list in the response.  This argument is a semi-column separated list of DICOM Tags identifiers; e.g: 'requested-tags=0010,0010;PatientBirthDate'.  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
                "short" (bool): If present, report the DICOM tags in hexadecimal format

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing information about the child DICOM series
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/series",
            params=params,
        )

    async def get_studies_id_shared_tags(
        self,
        id_: str,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get shared tags

        Extract the DICOM tags whose value is constant across all the child instances of the DICOM study whose Orthanc identifier is provided in the URL
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        params
            Dictionary of optional parameters:
                "short" (bool): If present, report the DICOM tags in hexadecimal format
                "simplify" (bool): If present, report the DICOM tags in human-readable format (using the symbolic name of the tags)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON object containing the values of the DICOM tags
        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/shared-tags",
            params=params,
        )

    async def post_studies_id_split(
        self,
        id_: str,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Split study

        Start a new job so as to split the DICOM study whose Orthanc identifier is provided in the URL, by taking some of its children series or instances out of it and putting them into a brand new study (this new study is created by setting the `StudyInstanceUID` tag to a random identifier): https://orthanc.uclouvain.be/book/users/anonymization.html#splitting
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Instances": The list of instances to be separated from the parent study. These instances must all be children of the same source study, that is specified in the URI.
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepSource": If set to `true`, instructs Orthanc to keep a copy of the original series/instances in the source study. By default, the original series/instances are deleted from Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Remove": List of tags that must be removed in the new study (from the same modules as in the `Replace` option)
              "Replace": Associative array to change the value of some DICOM tags in the new study. These tags must be part of the "Patient Module Attributes" or the "General Study Module Attributes", as specified by the DICOM 2011 standard in Tables C.7-1 and C.7-3.
              "Series": The list of series to be separated from the parent study. These series must all be children of the same source study, that is specified in the URI.
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/studies/{id_}/split",
            json=json,
        )

    async def get_studies_id_statistics(
        self,
        id_: str,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get study statistics

        Get statistics about the given study
        Tags: Studies

        Parameters
        ----------
        id_
            Orthanc identifier of the study of interest

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/studies/{id_}/statistics",
        )

    async def get_system(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get system information

        Get system information about Orthanc
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        return await self._get(
            route=f"{self.url}/system",
        )

    async def get_tools(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) List operations

        List the available operations under URI `/tools/`
        Tags: Other

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            List of the available operations
        """
        return await self._get(
            route=f"{self.url}/tools",
        )

    async def get_tools_accepted_sop_classes(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get accepted SOPClassUID

        Get the list of SOP Class UIDs that are accepted by Orthanc C-STORE SCP. This corresponds to the configuration options `AcceptedSopClasses` and `RejectedSopClasses`.
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the SOP Class UIDs
        """
        return await self._get(
            route=f"{self.url}/tools/accepted-sop-classes",
        )

    async def get_tools_accepted_transfer_syntaxes(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get accepted transfer syntaxes

        Get the list of UIDs of the DICOM transfer syntaxes that are accepted by Orthanc C-STORE SCP. This corresponds to the configuration options `AcceptedTransferSyntaxes` and `XXXTransferSyntaxAccepted`.
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the transfer syntax UIDs
        """
        return await self._get(
            route=f"{self.url}/tools/accepted-transfer-syntaxes",
        )

    async def put_tools_accepted_transfer_syntaxes(
        self,
        data: RequestData = None,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set accepted transfer syntaxes

        Set the DICOM transfer syntaxes that accepted by Orthanc C-STORE SCP
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:

        data
            UID of the transfer syntax to be accepted. Wildcards `?` and `*` are accepted.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the now-accepted transfer syntax UIDs
        """
        if json is None:
            json = {}
        return await self._put(
            route=f"{self.url}/tools/accepted-transfer-syntaxes",
            data=data,
            json=json,
        )

    async def post_tools_bulk_anonymize(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Anonymize a set of resources

        Start a job that will anonymize all the DICOM patients, studies, series or instances whose identifiers are provided in the `Resources` field.
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "DicomVersion": Version of the DICOM standard to be used for anonymization. Check out configuration option `DeidentifyLogsDicomVersion` for possible values.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": List of DICOM tags whose value must not be destroyed by the anonymization. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "KeepLabels": Keep the labels of all resources level (defaults to `false`)
              "KeepPrivateTags": Keep the private tags from the DICOM instances (defaults to `false`)
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of additional tags to be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Resources": List of the Orthanc identifiers of the patients/studies/series/instances of interest.
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The list of all the resources that have been created by this anonymization
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/bulk-anonymize",
            json=json,
        )

    async def post_tools_bulk_content(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Describe a set of resources

        Get the content all the DICOM patients, studies, series or instances whose identifiers are provided in the `Resources` field, in one single call.
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Level": This optional argument specifies the level of interest (can be `Patient`, `Study`, `Series` or `Instance`). Orthanc will loop over the items inside `Resources`, and explore upward or downward in the DICOM hierarchy in order to find the level of interest.
              "Metadata": If set to `true` (default value), the metadata associated with the resources will also be retrieved.
              "Resources": List of the Orthanc identifiers of the patients/studies/series/instances of interest.
              "Short": If set to `true`, report the DICOM tags in hexadecimal format


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/bulk-content",
            json=json,
        )

    async def post_tools_bulk_delete(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Delete a set of resources

        Delete all the DICOM patients, studies, series or instances whose identifiers are provided in the `Resources` field.
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Resources": List of the Orthanc identifiers of the patients/studies/series/instances of interest.


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/bulk-delete",
            json=json,
        )

    async def post_tools_bulk_modify(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Modify a set of resources

        Start a job that will modify all the DICOM patients, studies, series or instances whose identifiers are provided in the `Resources` field.
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, run the job in asynchronous mode, which means that the REST API call will immediately return, reporting the identifier of a job. Prefer this flavor wherever possible.
              "Force": Allow the modification of tags related to DICOM identifiers, at the risk of breaking the DICOM model of the real world
              "Keep": Keep the original value of the specified tags, to be chosen among the `StudyInstanceUID`, `SeriesInstanceUID` and `SOPInstanceUID` tags. Avoid this feature as much as possible, as this breaks the DICOM model of the real world.
              "KeepSource": If set to `false`, instructs Orthanc to the remove original resources. By default, the original resources are kept in Orthanc.
              "Level": Level of the modification (`Patient`, `Study`, `Series` or `Instance`). If absent, the level defaults to `Instance`, but is set to `Patient` if `PatientID` is modified, to `Study` if `StudyInstanceUID` is modified, or to `Series` if `SeriesInstancesUID` is modified. (new in Orthanc 1.9.7)
              "Permissive": If `true`, ignore errors during the individual steps of the job.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "PrivateCreator": The private creator to be used for private tags in `Replace`
              "Remove": List of tags that must be removed from the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "RemovePrivateTags": Remove the private tags from the DICOM instances (defaults to `false`)
              "Replace": Associative array to change the value of some DICOM tags in the DICOM instances. Starting with Orthanc 1.9.4, paths to subsequences can be provided using the same syntax as the `dcmodify` command-line tool (wildcards are supported as well).
              "Resources": List of the Orthanc identifiers of the patients/studies/series/instances of interest.
              "Synchronous": If `true`, run the job in synchronous mode, which means that the HTTP answer will directly contain the result of the job. This is the default, easy behavior, but it is *not* desirable for long jobs, as it might lead to network timeouts.
              "Transcode": Transcode the DICOM instances to the provided DICOM transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The list of all the resources that have been altered by this modification
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/bulk-modify",
            json=json,
        )

    async def post_tools_count_resources(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Count local resources

        This URI can be used to count the resources that are matching criteria on the content of the local Orthanc server, in a way that is similar to tools/find
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Labels": List of strings specifying which labels to look for in the resources (new in Orthanc 1.12.0)
              "LabelsConstraint": Constraint on the labels, can be `All`, `Any`, or `None` (defaults to `All`, new in Orthanc 1.12.0)
              "Level": Level of the query (`Patient`, `Study`, `Series` or `Instance`)
              "MetadataQuery": Associative array containing the filter on the values of the metadata (new in Orthanc 1.12.5)
              "ParentPatient": Limit the reported resources to descendants of this patient (new in Orthanc 1.12.5)
              "ParentSeries": Limit the reported resources to descendants of this series (new in Orthanc 1.12.5)
              "ParentStudy": Limit the reported resources to descendants of this study (new in Orthanc 1.12.5)
              "Query": Associative array containing the filter on the values of the DICOM tags
              "Short": If set to `true`, report the DICOM tags in hexadecimal format


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            A JSON object with the `Count` of matching resources
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/count-resources",
            json=json,
        )

    async def get_tools_create_archive(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Create a ZIP archive containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the 'resources' argument
        Tags: System

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "resources" (str): A comma separated list of Orthanc resource identifiers to include in the ZIP archive.
                "transcode" (str): If present, the DICOM files will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._get(
            route=f"{self.url}/tools/create-archive",
            params=params,
        )

    async def post_tools_create_archive(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create ZIP archive

        Create a ZIP archive containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the body
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": The list of Orthanc identifiers of interest.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/create-archive",
            json=json,
        )

    async def post_tools_create_dicom(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create one DICOM instance

        Create one DICOM instance, and store it into Orthanc
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Content": This field can be used to embed an image (pixel data encoded as PNG or JPEG), a PDF, or a 3D manufactoring model (MTL/OBJ/STL) inside the created DICOM instance. The file to be encapsulated must be provided using its [data URI scheme encoding](https://en.wikipedia.org/wiki/Data_URI_scheme). This field can possibly contain a JSON array, in which case a DICOM series is created containing one DICOM instance for each item in the `Content` field.
              "Force": Avoid the consistency checks for the DICOM tags that enforce the DICOM model of the real-world. You can notably use this flag if you need to manually set the tags `StudyInstanceUID`, `SeriesInstanceUID`, or `SOPInstanceUID`. Be careful with this feature.
              "InterpretBinaryTags": If some value in the `Tags` associative array is formatted according to some [data URI scheme encoding](https://en.wikipedia.org/wiki/Data_URI_scheme), whether this value is decoded to a binary value or kept as such (`true` by default)
              "Parent": If present, the newly created instance will be attached to the parent DICOM resource whose Orthanc identifier is contained in this field. The DICOM tags of the parent modules in the DICOM hierarchy will be automatically copied to the newly created instance.
              "PrivateCreator": The private creator to be used for private tags in `Tags`
              "Tags": Associative array containing the tags of the new instance to be created


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]

        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/create-dicom",
            json=json,
        )

    async def get_tools_create_media(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the 'resources' argument
        Tags: System

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "resources" (str): A comma separated list of Orthanc resource identifiers to include in the DICOMDIR media.
                "transcode" (str): If present, the DICOM files will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._get(
            route=f"{self.url}/tools/create-media",
            params=params,
        )

    async def post_tools_create_media(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the body
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Extended": If `true`, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*. Default value is `false`.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": The list of Orthanc identifiers of interest.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/create-media",
            json=json,
        )

    async def get_tools_create_media_extended(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the 'resources' argument
        Tags: System

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "resources" (str): A comma separated list of Orthanc resource identifiers to include in the DICOMDIR media.
                "transcode" (str): If present, the DICOM files will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._get(
            route=f"{self.url}/tools/create-media-extended",
            params=params,
        )

    async def post_tools_create_media_extended(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Create DICOMDIR media

        Create a DICOMDIR media containing the DICOM resources (patients, studies, series, or instances) whose Orthanc identifiers are provided in the body
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "Asynchronous": If `true`, create the archive in asynchronous mode, which means that a job is submitted to create the archive in background.
              "Extended": If `true`, will include additional tags such as `SeriesDescription`, leading to a so-called *extended DICOMDIR*. Default value is `true`.
              "Priority": In asynchronous mode, the priority of the job. The higher the value, the higher the priority.
              "Resources": The list of Orthanc identifiers of interest.
              "Synchronous": If `true`, create the archive in synchronous mode, which means that the HTTP answer will directly contain the ZIP file. This is the default, easy behavior. However, if global configuration option "SynchronousZipStream" is set to "false", asynchronous transfers should be preferred for large amount of data, as the creation of the temporary file might lead to network timeouts.
              "Transcode": If present, the DICOM files in the archive will be transcoded to the provided transfer syntax: https://orthanc.uclouvain.be/book/faq/transcoding.html


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            In asynchronous mode, information about the job that has been submitted to generate the archive: https://orthanc.uclouvain.be/book/users/advanced-rest.html#jobs
            In synchronous mode, the ZIP file containing the archive
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/create-media-extended",
            json=json,
        )

    async def get_tools_default_encoding(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get default encoding

        Get the default encoding that is used by Orthanc if parsing a DICOM instance without the `SpecificCharacterEncoding` tag, or during C-FIND. This corresponds to the configuration option `DefaultEncoding`.
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The name of the encoding
        """
        return await self._get(
            route=f"{self.url}/tools/default-encoding",
        )

    async def put_tools_default_encoding(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set default encoding

        Change the default encoding that is used by Orthanc if parsing a DICOM instance without the `SpecificCharacterEncoding` tag, or during C-FIND. This corresponds to the configuration option `DefaultEncoding`.
        Tags: System

        Parameters
        ----------
        data
            The name of the encoding. Check out configuration option `DefaultEncoding` for the allowed values.

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/default-encoding",
            data=data,
        )

    async def get_tools_dicom_conformance(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get DICOM conformance

        Get the DICOM conformance statement of Orthanc
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The DICOM conformance statement
        """
        return await self._get(
            route=f"{self.url}/tools/dicom-conformance",
        )

    async def post_tools_dicom_echo(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Trigger C-ECHO SCU

        Trigger C-ECHO SCU command against a DICOM modality described in the POST body, without having to register the modality in some `/modalities/{id}` (new in Orthanc 1.8.1)
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "AET": AET of the remote DICOM modality
              "CheckFind": Issue a dummy C-FIND command after the C-GET SCU, in order to check whether the remote modality knows about Orthanc. This field defaults to the value of the `DicomEchoChecksFind` configuration option. New in Orthanc 1.8.1.
              "Host": Host address of the remote DICOM modality (typically, an IP address)
              "LocalAet": Whether to override the default DicomAet in the SCU connection initiated by Orthanc to this modality
              "Manufacturer": Manufacturer of the remote DICOM modality (check configuration option `DicomModalities` for possible values
              "Port": TCP port of the remote DICOM modality
              "Timeout": Whether to override the default DicomScuTimeout in the SCU connection initiated by Orthanc to this modality
              "UseDicomTls": Whether to use DICOM TLS in the SCU connection initiated by Orthanc (new in Orthanc 1.9.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/dicom-echo",
            json=json,
        )

    async def post_tools_execute_script(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Execute Lua script

        Execute the provided Lua script by the Orthanc server. This is very insecure for Orthanc servers that are remotely accessible.  Since Orthanc 1.5.8, this route is disabled by default and can be enabled thanks to the `ExecuteLuaEnabled` configuration.
        Tags: System

        Parameters
        ----------
        data
            The Lua script to be executed

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Output of the Lua script
        """
        return await self._post(
            route=f"{self.url}/tools/execute-script",
            data=data,
        )

    async def post_tools_find(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Look for local resources

        This URI can be used to perform a search on the content of the local Orthanc server, in a way that is similar to querying remote DICOM modalities using C-FIND SCU: https://orthanc.uclouvain.be/book/users/rest.html#performing-finds-within-orthanc
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "CaseSensitive": Enable case-sensitive search for PN value representations (defaults to configuration option `CaseSensitivePN`)
              "Expand": If set to "true", retrieve detailed information about the individual resources, not only their Orthanc identifiers
              "Full": If set to `true`, report the DICOM tags in full format (tags indexed by their hexadecimal format, associated with their symbolic name and their value)
              "Labels": List of strings specifying which labels to look for in the resources (new in Orthanc 1.12.0)
              "LabelsConstraint": Constraint on the labels, can be `All`, `Any`, or `None` (defaults to `All`, new in Orthanc 1.12.0)
              "Level": Level of the query (`Patient`, `Study`, `Series` or `Instance`)
              "Limit": Limit the number of reported resources
              "MetadataQuery": Associative array containing the filter on the values of the metadata (new in Orthanc 1.12.5)
              "OrderBy": Array of associative arrays containing the requested ordering (new in Orthanc 1.12.5)
              "ParentPatient": Limit the reported resources to descendants of this patient (new in Orthanc 1.12.5)
              "ParentSeries": Limit the reported resources to descendants of this series (new in Orthanc 1.12.5)
              "ParentStudy": Limit the reported resources to descendants of this study (new in Orthanc 1.12.5)
              "Query": Associative array containing the filter on the values of the DICOM tags
              "RequestedTags": A list of DICOM tags to include in the response (applicable only if "Expand" is set to true).  The tags requested tags are returned in the 'RequestedTags' field in the response.  Note that, if you are requesting tags that are not listed in the Main Dicom Tags stored in DB, building the response might be slow since Orthanc will need to access the DICOM files.  If not specified, Orthanc will return all Main Dicom Tags to keep backward compatibility with Orthanc prior to 1.11.0.
              "ResponseContent": Defines the content of response for each returned resource. (this field, if present, overrides the "Expand" field).  Allowed values are `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`, `Attachments`.  If not specified, Orthanc will return `MainDicomTags`, `Metadata`, `Children`, `Parent`, `Labels`, `Status`, `IsStable`.(new in Orthanc 1.12.5)
              "Short": If set to `true`, report the DICOM tags in hexadecimal format
              "Since": Show only the resources since the provided index (in conjunction with `Limit`)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing either the Orthanc identifiers, or detailed information about the reported resources (if `Expand` argument is `true`)
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/find",
            json=json,
        )

    async def get_tools_generate_uid(
        self,
        params: QueryParamTypes = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Generate an identifier

        Generate a random DICOM identifier
        Tags: System

        Parameters
        ----------
        params
            Dictionary of optional parameters:
                "level" (str): Type of DICOM resource among: `patient`, `study`, `series` or `instance`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The generated identifier
        """
        return await self._get(
            route=f"{self.url}/tools/generate-uid_",
            params=params,
        )

    async def post_tools_invalid_ate_tags(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Invalidate DICOM-as-JSON summaries

        Remove all the attachments of the type "DICOM-as-JSON" that are associated will all the DICOM instances stored in Orthanc. These summaries will be automatically re-created on the next access. This is notably useful after changes to the `Dictionary` configuration option. https://orthanc.uclouvain.be/book/faq/orthanc-storage.html#storage-area
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/tools/invalid_ate-tags",
        )

    async def get_tools_labels(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get all the used labels

        List all the labels that are associated with any resource of the Orthanc database
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing the labels
        """
        return await self._get(
            route=f"{self.url}/tools/labels",
        )

    async def get_tools_log_level(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get main log level

        Get the main log level of Orthanc
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level",
        )

    async def put_tools_log_level(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set main log level

        Set the main log level of Orthanc
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level",
            data=data,
        )

    async def get_tools_log_level_dicom(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `dicom`

        Get the log level of the log category `dicom`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-dicom",
        )

    async def put_tools_log_level_dicom(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `dicom`

        Set the log level of the log category `dicom`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-dicom",
            data=data,
        )

    async def get_tools_log_level_generic(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `generic`

        Get the log level of the log category `generic`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-generic",
        )

    async def put_tools_log_level_generic(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `generic`

        Set the log level of the log category `generic`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-generic",
            data=data,
        )

    async def get_tools_log_level_http(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `http`

        Get the log level of the log category `http`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-http",
        )

    async def put_tools_log_level_http(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `http`

        Set the log level of the log category `http`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-http",
            data=data,
        )

    async def get_tools_log_level_jobs(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `jobs`

        Get the log level of the log category `jobs`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-jobs",
        )

    async def put_tools_log_level_jobs(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `jobs`

        Set the log level of the log category `jobs`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-jobs",
            data=data,
        )

    async def get_tools_log_level_lua(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `lua`

        Get the log level of the log category `lua`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-lua",
        )

    async def put_tools_log_level_lua(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `lua`

        Set the log level of the log category `lua`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-lua",
            data=data,
        )

    async def get_tools_log_level_plugins(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `plugins`

        Get the log level of the log category `plugins`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-plugins",
        )

    async def put_tools_log_level_plugins(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `plugins`

        Set the log level of the log category `plugins`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-plugins",
            data=data,
        )

    async def get_tools_log_level_sqlite(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get log level for `sqlite`

        Get the log level of the log category `sqlite`
        Tags: Logs

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            Possible values: `default`, `verbose` or `trace`
        """
        return await self._get(
            route=f"{self.url}/tools/log-level-sqlite",
        )

    async def put_tools_log_level_sqlite(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set log level for `sqlite`

        Set the log level of the log category `sqlite`
        Tags: Logs

        Parameters
        ----------
        data
            Possible values: `default`, `verbose` or `trace`

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/log-level-sqlite",
            data=data,
        )

    async def post_tools_lookup(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Look for DICOM identifiers

        This URI can be used to convert one DICOM identifier to a list of matching Orthanc resources
        Tags: System

        Parameters
        ----------
        data
            The DICOM identifier of interest (i.e. the value of `PatientID`, `StudyInstanceUID`, `SeriesInstanceUID`, or `SOPInstanceUID`)

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            JSON array containing a list of matching Orthanc resources, each item in the list corresponding to a JSON object with the fields `Type`, `ID` and `Path` identifying one DICOM resource that is stored by Orthanc
        """
        return await self._post(
            route=f"{self.url}/tools/lookup",
            data=data,
        )

    async def get_tools_metrics(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Are metrics collected?

        Returns a Boolean specifying whether Prometheus metrics are collected and exposed at `/tools/metrics-prometheus`
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `1` if metrics are collected, `0` if metrics are disabled
        """
        return await self._get(
            route=f"{self.url}/tools/metrics",
        )

    async def put_tools_metrics(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Enable collection of metrics

        Enable or disable the collection and publication of metrics at `/tools/metrics-prometheus`
        Tags: System

        Parameters
        ----------
        data
            `1` if metrics are collected, `0` if metrics are disabled

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/metrics",
            data=data,
        )

    async def get_tools_metrics_prometheus(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get usage metrics

        Get usage metrics of Orthanc in the Prometheus file format (OpenMetrics): https://orthanc.uclouvain.be/book/users/advanced-rest.html#instrumentation-with-prometheus
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            No description
        """
        return await self._get(
            route=f"{self.url}/tools/metrics-prometheus",
        )

    async def get_tools_now(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get UTC time

        Get UTC time
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The UTC time
        """
        return await self._get(
            route=f"{self.url}/tools/now",
        )

    async def get_tools_now_local(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Get local time

        Get local time
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            The local time
        """
        return await self._get(
            route=f"{self.url}/tools/now-local",
        )

    async def post_tools_reconstruct(
        self,
        json: Any = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Reconstruct all the index

        Reconstruct the index of all the tags of all the DICOM instances that are stored in Orthanc. This is notably useful after the deletion of resources whose children resources have inconsistent values with their sibling resources. Beware that this is a highly time-consuming operation, as all the DICOM instances will be parsed again, and as all the Orthanc index will be regenerated. If you have a large database to process, it is advised to use the Housekeeper plugin to perform this action resource by resource
        Tags: System

        Parameters
        ----------
        json
            Dictionary with the following keys:
              "ReconstructFiles": Also reconstruct the files of the resources (e.g: apply IngestTranscoding, StorageCompression). 'false' by default. (New in Orthanc 1.11.0)


        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        if json is None:
            json = {}
        return await self._post(
            route=f"{self.url}/tools/reconstruct",
            json=json,
        )

    async def post_tools_reset(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Restart Orthanc

        Restart Orthanc
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/tools/reset",
        )

    async def post_tools_shutdown(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Shutdown Orthanc

        Shutdown Orthanc
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._post(
            route=f"{self.url}/tools/shutdown",
        )

    async def get_tools_unknown_sop_class_accepted(
        self,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Is unknown SOP class accepted?

        Shall Orthanc C-STORE SCP accept DICOM instances with an unknown SOP class UID?
        Tags: System

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
            `1` if accepted, `0` if not accepted
        """
        return await self._get(
            route=f"{self.url}/tools/unknown-sop-class-accepted",
        )

    async def put_tools_unknown_sop_class_accepted(
        self,
        data: RequestData = None,
    ) -> Union[Dict, List, str, bytes, int, httpx.Response]:
        """(async) Set unknown SOP class accepted

        Set whether Orthanc C-STORE SCP should accept DICOM instances with an unknown SOP class UID
        Tags: System

        Parameters
        ----------
        data
            `1` if accepted, `0` if not accepted

        Returns
        -------
        Union[Dict, List, str, bytes, int, httpx.Response]
        """
        return await self._put(
            route=f"{self.url}/tools/unknown-sop-class-accepted",
            data=data,
        )

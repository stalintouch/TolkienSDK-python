import logging
import time
from dataclasses import dataclass
from os import environ
from urllib import parse
from datetime import datetime

from requests import Request
from requests import Response
from requests import Session
from rfc3339 import rfc3339

logger = logging.getLogger(__name__)


@dataclass
class SDKResponse:
    status_code: str
    ok: bool
    text: str


class SDKRequest():
    '''
        Provides an interface to interact with LOTR API
    '''
    user_session = Session()

    def __init__(self):
        self.BASE_URL = 'https://the-one-api.dev/v2'
        self.bearer_token = environ.get('BearerToken')

    def make_request(
        self, method, url, data={}, params=None, json=None
    ) -> Response:
        '''
            Makes request to LOTR API using the params passed

            Args:
                method: HTTP method
                url: endpoint to call
                data: data for post request
                params: params for filtering, pagination, sorting etc

            Returns either a Response object or a custom APIResponse the client can interact with
        '''
        request_url = ''.join([self.BASE_URL, url])
        headers = {
           'Authorization': f'Bearer {self.bearer_token}'
        }
        req = Request(
            method,
            request_url,
            data=data,
            params=params,
            headers=headers,
            json=json,
        )

        prepped_request = SDKRequest.user_session.prepare_request(req)
        resp = SDKRequest.user_session.send(prepped_request)

        duration = round(resp.elapsed.microseconds, 2)
        dt = datetime.fromtimestamp(time.time())
        timestamp = rfc3339(dt, utc=True)
        path = parse.urlparse(req.url).path

        logged_request = {
            'method': req.method,
            'path': path,
            'status': resp.status_code,
            'duration': duration,
            '@timestamp': timestamp,
            '@version': "1",
            'host': req.headers.get('Host'),
        }

        print(logged_request)

        return resp

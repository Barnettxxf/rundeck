from io import BytesIO

import demjson
import yaml

from bs4 import BeautifulSoup

from ..client import RundeckClient
from ..exceptions import ResponseError


class APIBase:
    def __init__(self, client: RundeckClient, api_version=19):
        assert api_version >= 19, 'API version must be greater than 18'
        self.api_version = api_version
        self.client = client

    def get_response(self, endpoint, method='get', **kwargs):
        func = getattr(self.client, method.lower())
        rsp = func(endpoint, **kwargs)
        if rsp.status_code == 204:
            return ''
        content_type = rsp.headers.get('Content-Type', '')
        if 'zip' in content_type:
            return rsp.content
        text = rsp.text
        if 'yaml' in content_type:
            text = yaml.safe_load(BytesIO(rsp.content))
        try:
            if isinstance(text, str):
                r = demjson.decode(text)
            else:
                r = text
        except demjson.JSONDecodeError:
            error = BeautifulSoup(text, 'html.parser')
            if 'xml' in content_type:
                error_text = error.find('message').text
            else:
                error_text = error.find('div', class_="text-danger").text.strip()
            raise ResponseError(error_text)
        if isinstance(r, dict) and r.get('error', False):
            raise ResponseError(r.get('message', ''))
        return r

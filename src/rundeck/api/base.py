from io import BytesIO

import demjson
import yaml

from bs4 import BeautifulSoup

from ..client import RundeckClient
from ..error import ResponseError


class APIBase:
    def __init__(self, client: RundeckClient, api_version=19):
        assert api_version >= 19, 'API version must be greater than 18'
        self.api_version = api_version
        self.client = client

    def get_response(self, endpoint, method='get', **kwargs):
        func = getattr(self.client, method.lower())
        rsp = func(endpoint, **kwargs)
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
            error = BeautifulSoup(text)
            raise ResponseError(error.find('div', class_="text-danger").text.strip())
        if isinstance(r, dict) and r.get('error', False):
            raise ResponseError(r.get('message', ''))
        return r

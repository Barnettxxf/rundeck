from .base import APIBase


class APIToken(APIBase):

    def list_tokens(self, user=None, options=None):
        endpoint = f'/api/{self.api_version}/tokens/{user}' if user else f'/api/{self.api_version}/tokens'
        return self.get_response(endpoint)

    def get_token(self, token_id, options=None):
        endpoint = f'/api/{self.api_version}/token/{token_id}'
        return self.get_response(endpoint)

    def create_token(self, user=None, options=None):
        endpoint = f'/api/{self.api_version}/tokens/{user}' if user else f'/api/{self.api_version}/tokens'
        headers = options.pop('headers', {'Content-type': 'application/json'})
        return self.get_response(endpoint, 'post', headers=headers, json=options)

    def delete_token(self, token_id, options=None):
        endpoint = f'/api/{self.api_version}/token/{token_id}'
        return self.get_response(endpoint, 'delete')

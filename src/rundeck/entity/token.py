from .base import Entity
from ..api.token import APIToken
from .item.token import TokenItem


class ListTokens(Entity):
    _api_cls = APIToken
    _item_cls = TokenItem
    _api_func_name = 'list_tokens'

    def __init__(self, client, user=None, options=None, api_version=19):
        super().__init__(client, user, options, api_version)

    @property
    def tokens(self):
        return self._result


class GetToken(Entity):
    _api_cls = APIToken
    _item_cls = TokenItem
    _api_func_name = 'get_token'

    def __init__(self, client, token_id, options=None, api_version=19):
        super().__init__(client, token_id, options, api_version)

    @property
    def token(self):
        return self._result


class CreateToken(Entity):
    _api_cls = APIToken
    _item_cls = TokenItem
    _api_func_name = 'create_token'

    def __init__(self, client, user=None, options=None, api_version=19):
        super().__init__(client, user, options, api_version)

    @property
    def result(self):
        return self._result


class DeleteToken(Entity):
    _api_cls = APIToken
    _api_func_name = 'delete_token'

    def __init__(self, client, token_id, options=None, api_version=19):
        super().__init__(client, token_id, options, api_version)

    @property
    def result(self):
        return self._result

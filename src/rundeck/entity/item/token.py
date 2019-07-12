from .base import Item, Field


class TokenItem(Item):
    user = Field()
    token = Field()
    id = Field()
    creator = Field()
    expiration = Field()
    roles = Field()
    expired = Field()

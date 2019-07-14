from .base import Item, Field


class TokenItem(Item):
    user = Field()
    token = Field()
    id = Field()
    creator = Field()
    expiration = Field()
    roles = Field()
    expired = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id}>'

    __str__ = __repr__

from ..item.base import Item, Field


class OptionsBase(Item):
    headers = Field()

    def _handle_not_set_field(self):
        pass

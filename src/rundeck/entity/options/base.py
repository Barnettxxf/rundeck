from ..item.base import Item, Field


class OptionsBase(Item):
    headers = Field()

    def _handle_not_set_field(self):
        for k, v in self.fields.items():
            if k not in self.keys() and v.default:
                self[k] = v.default


class EmptyOptions(Item):
    pass

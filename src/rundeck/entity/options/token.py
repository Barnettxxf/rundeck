from .base import OptionsBase, Field


class CreateTokenOption(OptionsBase):
    user = Field()
    roles = Field(default='*')
    duration = Field()

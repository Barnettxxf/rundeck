from abc import ABCMeta

import six


class Field:
    def __init__(self, type_=None, default=None):
        self.type = type_
        self.default = default

    def detect_type(self, value):
        if isinstance(self.type, list):
            assert value in self.type, f'{value} not in options({",".join(self.type)})'
        elif self.type is not None:
            return isinstance(value, self.type)
        return True

    def set_name(self, n):
        setattr(self, 'name', n)


class ItemMeta(ABCMeta):

    def __new__(mcs, class_name, bases, attrs):
        classcell = attrs.pop('__classcell__', None)
        new_bases = tuple(base._class for base in bases if hasattr(base, '_class'))
        _class = super(ItemMeta, mcs).__new__(mcs, 'x_' + class_name, new_bases, attrs)

        fields = getattr(_class, 'fields', {})
        new_attrs = {}
        for n in dir(_class):
            v = getattr(_class, n)
            if isinstance(v, Field):
                v.set_name(n)
                fields[n] = v
            elif n in attrs:
                new_attrs[n] = attrs[n]

        new_attrs['fields'] = fields
        new_attrs['_class'] = _class
        if classcell is not None:
            new_attrs['__classcell__'] = classcell
        return super(ItemMeta, mcs).__new__(mcs, class_name, bases, new_attrs)


class DictItem(dict):
    skip_error = True

    fields = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            self._set_fields(k, v)
        self._handle_not_set_field()

    def _set_fields(self, k, v):
        k = k.replace('-', '_')
        assert k in self.fields.keys() or self.skip_error, 'Not support field %s' % k
        if not self.skip_error:
            assert self.fields[k].detect_type(v), f'Got an unexpected type value for {k}, ' \
                f'expected {self._fields_mapping[k].type}'
        self[k] = v

    def _handle_not_set_field(self):
        for f in self.fields.keys():
            if f not in self.keys():
                self[f] = None

    def __getattr__(self, item):
        if item not in self.keys():
            raise AttributeError('Not found attribute %s' % item)
        return self[item]

    def to_dict(self):
        return dict(self)

    def copy(self):
        return self.__class__(**self.to_dict())

    def __repr__(self):
        return f'<{self.__class__.__name__} ({id(self)})>'

    __str__ = __repr__


@six.add_metaclass(ItemMeta)
class Item(DictItem):
    pass

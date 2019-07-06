class EntityBase:
    api_cls = None

    def __init__(self, client, api_version=19):
        assert self.api_cls
        self.api = self.api_cls(client, api_version)
        self._data = None

    @property
    def data(self):
        return self._data


class EntityWithProjectName(EntityBase):
    item_cls = None
    api_func_name = None

    def __init__(self, project_name, client, options=None,api_version=19):
        assert self.item_cls
        assert self.api_func_name
        super().__init__(client, api_version)
        self._init(project_name, options)

    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, pn):
        self._init(pn)

    def _init(self, pn, o):
        self._project_name = pn
        self._data = getattr(self.api, self.api_func_name)(pn, o)
        if self.item_cls:
            self._result = [self.item_cls(**x) for x in self._data] if isinstance(self._data, list) else self.item_cls(
                **self._data)
        else:
            self._result = self._data


class EntityWithJobID(EntityBase):
    item_cls = None

    def __init__(self, job_id, client, options=None, api_version=19):
        super().__init__(client, api_version)
        self.job_id = job_id

class Entity:
    api_cls = None
    item_cls = None
    api_func_name = None
    paging_cls = None
    options_cls = None
    result_key = 'executions'

    def __init__(self, client, itm_id, options=None, api_version=19):
        assert self.api_cls
        assert self.api_func_name

        self.api = self.api_cls(client, api_version)

        self.client = client
        self.api_version = api_version
        self.options = options

        self._init(itm_id, options)

    def _init(self, itm_id, o):
        self._itm_id = itm_id
        self._data = getattr(self.api, self.api_func_name)(itm_id, o)
        if self.item_cls:
            if self.paging_cls:
                self._page = self.paging_cls(**self._data['paging'])
                self._result = [self.item_cls(**x) for x in self._data[self.result_key]]
            else:
                self._result = [self.item_cls(**x) for x in self._data] \
                    if isinstance(self._data, list) else self.item_cls(**self._data)
        else:
            self._result = self._data

    def asset_options(self):
        if self.options_cls:
            assert isinstance(self.options, self.options_cls)

    @property
    def data(self):
        return self._data


class EntityWithProjectName(Entity):

    def __init__(self, client, project_name, options=None, api_version=19):
        super().__init__(client, project_name, options, api_version)

    @property
    def project_name(self):
        return self._itm_id

    @project_name.setter
    def project_name(self, pn):
        self._init(pn, self.options)


class EntityWithJobId(Entity):

    def __init__(self, client, job_id, options=None, api_version=19):
        super().__init__(client, job_id, options, api_version)

    @property
    def job_id(self):
        return self._itm_id

    @job_id.setter
    def job_id(self, jid):
        self._init(jid, self.options)


class EntityWithExecId(Entity):

    def __init__(self, client, exec_id, options=None, api_version=19):
        super().__init__(client, exec_id, options, api_version)

    @property
    def exec_id(self):
        return self._itm_id

    @exec_id.setter
    def exec_id(self, eid):
        self._init(eid, self.options)

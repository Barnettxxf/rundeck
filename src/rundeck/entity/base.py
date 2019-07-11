import io


class Entity:
    _api_cls = None
    _item_cls = None
    _api_func_name = None
    _paging_cls = None
    _options_cls = None
    _result_key = 'executions'

    def __init__(self, client, itm_id, options=None, api_version=19):
        assert self._api_cls
        assert self._api_func_name

        self.api = self._api_cls(client, api_version)

        self.client = client
        self.api_version = api_version
        self.options = options

        self._init(itm_id, options)

    def _init(self, itm_id, o):
        self._itm_id = itm_id
        self._data = getattr(self.api, self._api_func_name)(itm_id, o)
        if self._item_cls:
            if self._paging_cls:
                self._page = self._paging_cls(**self._data['paging'])
                self._result = [self._item_cls(**x) for x in self._data[self._result_key]]
            else:
                self._result = [self._item_cls(**x) for x in self._data] \
                    if isinstance(self._data, list) else self._item_cls(**self._data)
        else:
            if isinstance(self._data, bytes):
                self._result = io.BytesIO(self._data)
            else:
                self._result = self._data

    def asset_options(self):
        if self._options_cls:
            assert isinstance(self.options, self._options_cls)

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

import io


def test_create_delete_project(rd):
    from rundeck.entity.options.project import ProjectCreationOptions
    project_name = 'hahahahha'
    options = ProjectCreationOptions(
        name=project_name
    )
    r = rd.create_project(options=options)
    assert r.project_info

    rd.delete_project(project_name)


def test_list_project(rd):
    lp = rd.list_projects()

    assert lp.data
    assert lp.projects
    assert lp.project_names


def test_project_info(rd):
    lp = rd.project_info(rd.list_projects().project_names[-1])

    assert lp.data
    assert lp.project_info
    assert lp.project_name


def test_project_resource(rd):
    lp = rd.list_project_resource(rd.list_projects().project_names[-1])

    assert lp.data
    assert lp.project_name
    assert lp.resources


def test_project_export(rd):
    project_name = rd.list_projects().project_names[-1]
    lp = rd.export_project(project_name)

    assert isinstance(lp.data, bytes)
    assert isinstance(lp.zip_stream, io.BytesIO)
    with open(f'{project_name}.zip', 'wb') as f:
        f.write(lp.data)


def test_project_import(rd):
    from rundeck.entity.options.project import ProjectCreationOptions
    project_name = 'hahahahha'
    options = ProjectCreationOptions(
        name=project_name
    )
    r = rd.create_project(options=options)
    assert r.project_info

    from rundeck.entity.options.project import ProjectArchiveImportOption
    with open('or.zip', 'rb') as f:
        options = ProjectArchiveImportOption(
            jobUuidOption='remove',
            importExecutions=True,
            importConfig=True,
            importACL=True,
            importScm=True,
            file=f.read()
        )
        lp = rd.import_project(project_name, options=options)
        assert lp.data
        assert lp.status

    rd.delete_project(project_name)


def test_project_export_async(rd):
    project_name = rd.list_projects().project_names[-1]

    from rundeck.entity.options.project import ProjectArchiveExportAsyncOptions
    options = ProjectArchiveExportAsyncOptions(
        exportAll=True,
        exportJobs=True,
        exportExecutions=True,
        exportConfigs=True,
        exportReadmes=True,
        exportAcls=True,
        exportScm=True,
    )

    lp = rd.export_project_async(project_name, options=options)

    assert lp.status

    from rundeck.entity.options.project import ProjectArchiveExportAsyncStatusOptions
    options = ProjectArchiveExportAsyncStatusOptions(
        token=lp.status.token
    )
    lp = rd.get_status_of_export_async(project_name, options=options)
    assert lp.status

    while True:
        if not lp.refresh().ready:
            continue

        from rundeck.entity.options.project import ProjectArchiveExportAsyncDownloadOptions
        options = ProjectArchiveExportAsyncDownloadOptions(
            token=lp.status.token
        )
        lp = rd.download(project_name, options)
        with open(f'{project_name}.zip', 'wb') as f:
            f.write(lp.data)

        break

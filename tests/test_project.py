import io

from rundeck.entity import project


def test_list_project(cli):
    lp = project.ProjectList(cli)

    assert lp.data
    assert lp.projects
    assert lp.project_names


def test_project_info(cli):
    lp = project.ProjectInfo(cli, 'Spider')

    assert lp.data
    assert lp.project_info
    assert lp.project_name


def test_project_resource(cli):
    lp = project.ProjectResources(cli, 'Spider')

    assert lp.data
    assert lp.project_name
    assert lp.resources


def test_project_export(cli):
    project_name = project.ProjectList(cli).project_names[-1]
    lp = project.ProjectArchiveExport(cli, project_name)

    assert isinstance(lp.data, bytes)
    assert isinstance(lp.zip_stream, io.BytesIO)
    with open(f'{project_name}.zip', 'wb') as f:
        f.write(lp.data)


def test_project_import(cli):
    from rundeck.entity.options.project import ProjectArchiveImportOption
    with open('Spider.zip', 'rb') as f:
        options = ProjectArchiveImportOption(
            jobUuidOption='remove',
            importExecutions=True,
            importConfig=True,
            importACL=True,
            importScm=True,
            file=f.read()
        )
        lp = project.ProjectArchiveImport(cli, 'test', options=options)
        assert lp.data
        assert lp.status


def test_project_export_async(cli):
    project_name = project.ProjectList(cli).project_names[-1]

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

    lp = project.ProjectArchiveExportAsync(cli, project_name, options=options)

    assert lp.status

    from rundeck.entity.options.project import ProjectArchiveExportAsyncStatusOptions
    options = ProjectArchiveExportAsyncStatusOptions(
        token=lp.status.token
    )
    lp = project.ProjectArchiveExportAsyncStatus(cli, project_name, options=options)
    assert lp.status

    while True:
        if not lp.refresh().ready:
            continue

        from rundeck.entity.options.project import ProjectArchiveExportAsyncDownloadOptions
        options = ProjectArchiveExportAsyncDownloadOptions(
            token=lp.status.token
        )
        lp = project.ProjectArchiveExportAsyncDownload(cli, project_name, options=options)
        with open(f'{project_name}.zip', 'wb') as f:
            f.write(lp.data)

        break



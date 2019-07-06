from rundeck.entity import project


def test_list_project(cli):
    lp = project.ProjectList(cli)

    assert lp.data
    assert lp.projects
    assert lp.project_names


def test_project_info(cli):
    lp = project.ProjectInfo('or', cli)

    assert lp.data
    assert lp.project_info
    assert lp.project_name


def test_project_resource(cli):
    lp = project.ProjectResources('or', cli)

    assert lp.data
    assert lp.project_name
    assert lp.resources

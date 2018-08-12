from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.return_home()
    old_projects = app.project.get_project_list()
    app.project.create_project(Project(name="Test5", description="test"))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
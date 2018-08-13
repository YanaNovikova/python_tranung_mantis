from model.project import Project


def test_add_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as("administrator")
    app.project.return_home()
    old_projects = app.soap.can_list(username, password)
    app.project.create_project(Project(name="Test5", description="test"))
    new_projects = app.soap.can_list(username, password)
    assert len(old_projects) + 1 == len(new_projects)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
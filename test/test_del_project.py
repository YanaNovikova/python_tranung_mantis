from model.project import Project
import random


def test_del_projects(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as("administrator")
    app.project.return_home()
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="Test5", description="test"))
    old_projects = app.soap.can_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = app.soap.can_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)



def test_login(app):
    app.session.login("adminictrator", "root")
    assert app.session.is_logged_in_as("adminictrator")
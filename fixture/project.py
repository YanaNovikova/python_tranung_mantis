from model.project import Project
import re

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_link_text("Create New Project").click()

    def change_field_value_project(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value_project("name", project.name)
        self.change_field_value_project("description", project.description)

    def create_project(self, contact):
        wd = self.app.wd
        self.return_home()
        self.open_project_page()
        # fill contact form
        self.fill_project_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.return_home()
        self.select_project_by_id(id)
        # submit delete
        wd.find_element_by_link_text("Delete Project").click()
        wd.switch_to_alert().accept()
        self.return_home()
        self.contact_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("tr.row-2 > td > a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()
        
    def return_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("//manage_proj_page.php") and len(wd.find_elements_by_name("Create New Project")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

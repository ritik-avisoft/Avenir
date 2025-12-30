from playwright.sync_api import Page,expect

class BasePage:
    def __init__(self,page:Page):
        self.page = page
        self.page_main_logo=page.locator(".flex.cursor-pointer")
        self.page_login_button=page.get_by_role("button", name="Login")

    def open_login_side_bar(self):
        self.page_login_button.click()
    
    def login(self, email, password):
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
    

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, user="standard_user", password="secret_sauce"):
        self.page.fill("#user-name", user)
        self.page.fill("#password", password)
        self.page.click("#login-button")
        

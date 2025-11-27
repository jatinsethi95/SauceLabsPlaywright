from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_information(self, first="John", last="Doe", zip="12345"):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip)
        self.page.click("#continue")

    def finish_checkout(self):
        self.page.click("#finish")

    def get_success_message(self):
        return self.page.locator(".complete-header").inner_text()

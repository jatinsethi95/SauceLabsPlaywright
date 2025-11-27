from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_cart_items(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def checkout(self):
        self.page.click("#checkout")

import random
from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")

    def add_random_items(self, count=3):
        item_count = self.inventory_items.count()
        indices = random.sample(range(item_count), count)

        selected_items = []
        for index in indices:
            item = self.inventory_items.nth(index)
            title = item.locator(".inventory_item_name").inner_text()
            item.locator("button").click()
            selected_items.append(title)

        return selected_items

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")

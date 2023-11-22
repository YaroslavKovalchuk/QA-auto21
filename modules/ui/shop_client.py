from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.rozetka_cart_page import CartPage
from modules.ui.page_objects.rozetka_product_page import ProductPage


class ShopClient:
        
    def __init__(self) -> None:
        self.base = BasePage()
        self.product_page = ProductPage(self.base.driver)
        self.cart_page = CartPage(self.base.driver)

    def add_product_to_cart(self):
            self.product_page.go_to()
            self.product_page.add_a_product_to_a_cart()
            self.cart_page.go_to()
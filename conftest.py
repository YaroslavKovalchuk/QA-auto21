import pytest
from modules.common.database import Database
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.rozetka_cart_page import CartPage
from modules.ui.page_objects.rozetka_product_page import ProductPage

from tests.api.clients.github2 import GitHub

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture()
def github_api():
    api = GitHub()
    yield api

@pytest.fixture()
def database():
    db = Database()
    yield db

class ShopClient:
        
    def __init__(self) -> None:
        self.base = BasePage()
        self.product_page = ProductPage(self.base.driver)
        self.cart_page = CartPage(self.base.driver)

    def add_product_to_cart(self):
            self.product_page.go_to()
            self.product_page.add_a_product_to_a_cart()
            self.cart_page.go_to()


@pytest.fixture()
def rozetka_cart():
    client = ShopClient()
    client.add_product_to_cart()
    yield client
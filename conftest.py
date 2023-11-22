import pytest
from modules.common.database import Database
from modules.api.clients.github import GitHub
from modules.ui.shop_client import ShopClient
from modules.ui.user import User


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


@pytest.fixture()
def rozetka_cart_with_item():
    client = ShopClient()
    client.add_product_to_cart()
    yield client
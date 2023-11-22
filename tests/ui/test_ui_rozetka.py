from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.rozetka_cart_page import CartPage
from modules.ui.page_objects.rozetka_product_page import ProductPage
import pytest

# Індивідуальна частина проєктного завдання

@pytest.mark.ui_rozetka
def test_cart_title(rozetka_cart_with_item):
    assert rozetka_cart_with_item.cart_page.check_title("Ноутбук Acer Aspire 7 A715-76G-56U7 (NH.QN4EU.001) Charcoal Black / Intel Core i5-12450H / RAM 16 ГБ / SSD 512 ГБ / nVidia GeForce RTX 2050, 4 ГБ / Підсвічування клавіатури")


@pytest.mark.ui_rozetka
def test_delete_product_from_a_cart(rozetka_cart_with_item):
    assert rozetka_cart_with_item.cart_page.check_to_delete_product("Кошик порожній")


@pytest.mark.ui_rozetka
def test_checkout_btn(rozetka_cart_with_item):
    assert rozetka_cart_with_item.cart_page.check_checkout_btn("https://rozetka.com.ua/ua/checkout/")


@pytest.mark.ui_rozetka
def test_negative_sum_receipt_calc_in_cart(rozetka_cart_with_item):
    assert rozetka_cart_with_item.cart_page.check_sum_receipt_calc(-1)

@pytest.mark.ui_rozetka
def test_zero_sum_receipt_calc_in_cart(rozetka_cart_with_item):
    assert rozetka_cart_with_item.cart_page.check_sum_receipt_calc(0)

@pytest.mark.ui_rozetka
def test_positive_sum_receipt_calc_in_cart(rozetka_cart_with_item):  
    assert rozetka_cart_with_item.cart_page.check_sum_receipt_calc(2)
    


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


class CartPage():

    URL = "https://rozetka.com.ua/ua/cart/"

    def __init__(self, driver:webdriver.Chrome) -> None:
        self.driver = driver
    

    def go_to(self):
        self.driver.get(CartPage.URL)
        

    def check_title(self, expected_title):

        product = self.driver.find_element(By.CLASS_NAME, "cart-product__title")

        return product.get_attribute("title") == expected_title
    

    def check_sum_receipt_calc(self, qnt):

        receipt_sum = self.driver.find_element(By.XPATH, "//div[@data-testid='cart-receipt-sum']").text
        old_price = int(str(receipt_sum).replace('₴','').replace(" ", ""))

        qnt_field = self.driver.find_element(By.XPATH, "//input[@data-testid='cart-counter-input']")
        qnt_field.clear()
        qnt_field.send_keys(qnt)

        time.sleep(5)

        receipt_sum_new= self.driver.find_element(By.XPATH, "//div[@data-testid='cart-receipt-sum']").text
        new_price = int(str(receipt_sum_new).replace('₴','').replace(" ", ""))

        if(qnt <= 1):
            return old_price == new_price
        else:
            res = old_price * qnt
            return new_price == res

    
    def check_checkout_btn(self, ecxpected_url):
        
        checkout_btn = self.driver.find_element(By.XPATH,  "//a[@class='button button--green button_size_large cart-receipt__submit']")
        checkout_btn.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ecxpected_url))
        except TimeoutException:
            print('Timeout exception has occurred')

        return self.driver.current_url == ecxpected_url



    def check_to_delete_product(self, expect_msg):

        action_btn = self.driver.find_element(By.ID, "cartProductActions0")
        action_btn.click()

        delete_btn = self.driver.find_element(By.CLASS_NAME, "popup-menu__list")
        delete_btn.click()

        try:
            cart_caption = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='empty-cart']")))
            print(cart_caption.text)
        except TimeoutException:
             print('Timeout exception has occurred')
        
        return expect_msg in cart_caption.text

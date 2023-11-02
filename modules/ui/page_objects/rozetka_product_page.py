from selenium.webdriver.common.by import By
from selenium import webdriver


class ProductPage():

    URL = "https://rozetka.com.ua/ua/acer-nhqn4eu001/p391395969/"

    def __init__(self, driver:webdriver.Chrome) -> None:
        self.driver = driver
    
    def go_to(self):
        self.driver.get(ProductPage.URL)


    def add_a_product_to_a_cart(self):      
        btn_buy = self.driver.find_element(By.CLASS_NAME, "buy-button")
        btn_buy.click()

    def check_opening_cart_modal_window(self):
        modal_elem = self.driver.find_element(By.CLASS_NAME, "modal__heading")
        print(modal_elem.text)

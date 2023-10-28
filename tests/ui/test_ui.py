import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorect_username():
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    
    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")

    login_elem.send_keys("kovalchukya1995@email.com")

    password_elem = driver.find_element(By.ID, "password")

    password_elem.send_keys("wrong password")

    btn_elem = driver.find_element(By.NAME, "commit")

    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(2)

    driver.close()
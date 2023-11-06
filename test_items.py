import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_button_add_to_cart_is_presented(browser, user_language):
    link = f"https://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)

    button_add = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button_add != None, "No such element"


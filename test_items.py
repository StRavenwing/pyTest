import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_items(browser,language):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    button_add = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form>button")
    assertTrue (button_add!=None, "No such element")


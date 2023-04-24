import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(param):
    return str(math.log(abs(12*math.sin(int(param)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id=input_value]")
    x = x_element.text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
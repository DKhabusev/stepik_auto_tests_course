from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(param1, param2):
    return int(param1) + int(param2)


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    first_num = browser.find_element(By.CSS_SELECTOR, "span[id=num1]").text
    second_num = browser.find_element(By.CSS_SELECTOR, "span[id=num2]").text
    summa = calc(first_num, second_num)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(summa))
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1_in_text = browser.find_element(By.ID, "num1")
num2_in_text = browser.find_element(By.ID, "num2")

num1 = int(num1_in_text.text)
num2 = int(num2_in_text.text)

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(num1 + num2))

send_button = browser.find_element(By.CLASS_NAME, "btn-default")
send_button.click()

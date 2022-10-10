from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name_field = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
lastname_field = browser.find_element(By.CSS_SELECTOR,"[name='lastname']")
email_field = browser.find_element(By.CSS_SELECTOR,"[name='email']")
file_button = browser.find_element(By.CSS_SELECTOR,"[type='file']")
send_button = browser.find_element(By.CSS_SELECTOR,".btn-primary")

name_field.send_keys("H")
lastname_field.send_keys("F")
email_field.send_keys("y")

current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, "test_file.txt")

file_button.send_keys(file_path)
send_button.click()
time.sleep(30)

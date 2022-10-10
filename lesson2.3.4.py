from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
	return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

magic_button = browser.find_element(By.CLASS_NAME, "btn-primary")
magic_button.click()

time.sleep(1)

alert = browser.switch_to.alert
alert.accept()

x_string = browser.find_element(By.ID, "input_value")
x_number = int( x_string.text )

answer = calc(x_number)

input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(answer)

send_button = browser.find_element(By.CLASS_NAME, "btn-primary")
send_button.click()

time.sleep(1)

alert = browser.switch_to.alert
alert_text = alert.text

addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

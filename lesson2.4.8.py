from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

x_string = browser.find_element(By.ID, "input_value")
x_number = int(x_string.text)

def calc(x):
	return str (math.log(abs(12 * math.sin(int(x)))))

answer = calc(x_number)

input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(answer)

send_button = browser.find_element(By.ID, "solve")
send_button.click()

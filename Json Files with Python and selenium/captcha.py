import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from solveRecaptcha import solveRecaptcha


browser = webdriver.Chrome()
browser.get("https://google.com/recaptcha/api2/demo")

result = solveRecaptcha(
    "6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u",
    'https://google.com/recaptcha/api2/demo',
)

code = result['code']

print(code)

WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located(By.ID, 'g-recaptcha-response')
)

browser.execute_script(
    "document.getElementById('g-recaptcha-response').innerHMTL =    " +
    "'" + code + "'"
)

time.sleep(5)

browser.find_element(By.ID, "recaptcha-demo-submit").click()

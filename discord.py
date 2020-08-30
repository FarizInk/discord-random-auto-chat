

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import sentences
import user
import time
import random

driver = webdriver.Chrome('/usr/bin/chromedriver')
actions = ActionChains(driver)

driver.get("https://discord.com/login")
inputName = driver.find_element_by_name("email")
inputName.clear()
inputName.send_keys(user.email)
inputPass = driver.find_element_by_name("password")
inputPass.clear()
inputPass.send_keys(user.password)
inputPass.send_keys(Keys.RETURN)


wait = WebDriverWait(driver, 10)
element = wait.until(EC.url_changes("https://discord.com/login"))

driver.get("https://discord.com/channels/number/number")
time.sleep(7)

theBody = driver.find_element_by_tag_name('body')
try:
    while True:
        text = random.choice(sentences)
        textArea = driver.find_elements_by_css_selector("div[class^=textArea-]")[0]
        textArea.find_elements_by_css_selector("div")[2].click()
        print("-> Clicked Text Area")
        print("-> Write: " + text)
        theBody.send_keys(text)
        actions.send_keys(Keys.RETURN)
        print("-> Sending Text")
        actions.perform()

        print("----------------------------------")
        time.sleep(3)
except KeyboardInterrupt:
    driver.close()
    pass

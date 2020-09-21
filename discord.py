

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import sentences
# import conf
import time
import random

import yaml

with open("conf.yaml", 'r') as stream:
    try:
        conf=yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if conf['os'] == 'linux':
    driver = webdriver.Chrome(conf['linuxChromeDriverPath'])
else:
    driver = webdriver.Chrome('chromedriver.exe')
    
actions = ActionChains(driver)

driver.get("https://discord.com/login")
inputName = driver.find_element_by_name("email")
inputName.clear()
inputName.send_keys(conf['email'])
inputPass = driver.find_element_by_name("password")
inputPass.clear()
inputPass.send_keys(conf['password'])
inputPass.send_keys(Keys.RETURN)


wait = WebDriverWait(driver, 10)
element = wait.until(EC.url_changes("https://discord.com/login"))

driver.get(conf['channel'])
time.sleep(7)

theBody = driver.find_element_by_tag_name('body')

count = 1

try:
    while True:
        if conf['customMessage'] != "":
            text = conf['customMessage']
        else:
            text = random.choice(sentences)
        textArea = driver.find_elements_by_css_selector("div[class^=textArea-]")[0]
        textArea.find_elements_by_css_selector("div")[2].click()
        print("-> Clicked Text Area")
        print("-> Write: " + text)
        theBody.send_keys(text)
        actions.send_keys(Keys.RETURN)
        print("-> Sending Text")
        actions.perform()


        print("-> Count: " + str(count))
        count += 1
        print("----------------------------------")

        if conf['loop'] is not None :
            if conf['loop'] >= count:
                pass
            else:
                time.sleep(conf['delayinsecond'])
                break

        time.sleep(conf['delayinsecond'])
except KeyboardInterrupt:
    driver.close()
    pass

driver.close()
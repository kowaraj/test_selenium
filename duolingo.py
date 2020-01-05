
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import credentials

def pick_my_darling(driver):
    i=0
    while(1):
        e = driver.find_element_by_class_name("challenge-answers li:nth-of-type("+str(i)+")")
        if e.text == 'My darling.':
            e.click()
            break
        i = i+1
        if i > 3:
            exit(0)
        input("next?")
        
def run():
    driver = webdriver.Chrome()
    input("next?")

    driver.get("https://www.duolingo.com/course/ja/en/Learn-Japanese")
    driver.set_window_size(1280, 773)
    input("next?")

    # 3 | mouseOver | css=.\_2hNaj |  | 
    element = driver.find_element(By.CSS_SELECTOR, ".\\_2hNaj")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    input("next?")

    # Click "Already have an account"
    input("next? - push 'have-account'")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"have-account\"]").click()

    # Provide the credentials
    input("next? - credentials")
    l = credentials.get_login()
    print("l = " + str(l))
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"email-input\"]").send_keys(l)

    input("next? - credentials")
    p = credentials.get_password()
    print("p = " + str(p))
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password-input\"]").send_keys(p)
    input("next? - credentials")


    # Click "Login"
    input("next? - login")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"register-button\"]").click()
    input("next? - 1")
    element = driver.find_element(By.CSS_SELECTOR, ".\\_3ryeM")
    input("next? - 1")
    actions = ActionChains(driver)
    input("next? - 1")
    actions.move_to_element(element).perform()
    input("next? - 1")

    input("next? - ...")
    element = driver.find_element(By.CSS_SELECTOR, ".Xpzj7:nth-child(1) .\\_2GJb6:nth-child(1)")
    input("next? - 1")
    actions = ActionChains(driver)
    input("next? - 1")
    actions.move_to_element(element).perform()

    input("next? - ...")
    # 9 | mouseOut | css=.Xpzj7:nth-child(1) .\_2GJb6:nth-child(1) |  | 
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)


    # Switch to French/Chinese (9/11)
    # input("next? - to french")
    # element = driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(11)")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()

    # element = driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(9)")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()

    # Switch to the "Stories"
    input("next? - to stories")
    element = driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(3) .\\_1KHTi")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(3) .\\_1KHTi").click()

    # Scroll to y=1 line
    input("next? - scroll to the beginning of the page")
    driver.execute_script("window.scrollTo(0,1)")
    
    # Start the first story
    input("next? - start the first story")
    driver.find_element(By.CSS_SELECTOR, ".set:nth-child(2) > .story:nth-child(3) .story-cover-illustration-image").click()

    # Click the 'CONTINUE' button
    input("next? - 1/3")
    driver.find_element_by_class_name("continue").click()
    input("next? - 2/3")
    driver.find_element_by_class_name("continue").click()
    input("next? - 3/3")
    driver.find_element_by_class_name("continue").click()

    # Choose a checkbox 
    input("next? - ")
    element = driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button").click()

    # 
    input("next? - 1/3")
    driver.find_element_by_class_name("continue").click()
    input("next? - 2/3")
    driver.find_element_by_class_name("continue").click()
    input("next? - 3/3")
    driver.find_element_by_class_name("continue").click()

    # Choose a selectable-token

    # element = driver.find_element(By.CSS_SELECTOR, ".challenge-answer:nth-child(1) > .selectable-token")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).release().perform()
    # driver.find_element(By.CSS_SELECTOR, ".challenge-answer:nth-child(1) > .selectable-token").click()

    # >>> driver.find_element_by_class_name("challenge-answers li:nth-of-type(2)").text
    # 'My brother.'
    # >>> driver.find_element_by_class_name("challenge-answers li:nth-of-type(1)").text
    # 'My colleague.'
    # >>> driver.find_element_by_class_name("challenge-answers li:nth-of-type(3)").text
    # 'My darling.'


    input("next?")

    pick_my_darling(driver)

    input("next?")

    # 
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()

    # Choose a word
    element = driver.find_element(By.CSS_SELECTOR, ".phrase:nth-child(6) .point-to-phrase-synced-text")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".phrase:nth-child(6) .point-to-phrase-synced-text").click()

    # 
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()

    # a PAUSE here to listen "Marion mets du sucre dans sa tasse"

    # 
    driver.find_element_by_class_name("continue").click()

    # Choose a checkbox "She put sugar in her coffee"
    element = driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button").click()

    # 
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()

    # Choose a checkbox for "quoi = What?"
    element = driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button").click()

    # 
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()
    driver.find_element_by_class_name("continue").click()

    # Choose a checkbox "Marion was so tired that shee... put solt in her coffee"
    element = driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button").click()

    # 
    driver.find_element_by_class_name("continue").click()

    # Match the words.......
    #
    #
    #

    # 
    driver.find_element_by_class_name("continue").click() # Done
    driver.find_element_by_class_name("continue").click() # You earned 24 XP
    driver.find_element_by_class_name("continue").click() # Story complete!
    driver.find_element_by_class_name("continue").click() # Back to "Stories"




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

class Duolingo:

    def __init__(self, b):
        if b == 'Chrome':
            self.driver = webdriver.Chrome()
        elif b == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            exit(-1)

        input('goto duolingo')
        self.driver.get("https://duolingo.com")
        time.sleep(2)
        self.driver.set_window_size(1280, 773)

    def get_driver(self):
        return self.driver

    def click_alread_have_an_account(self):
        #input("next? - push 'have-account'")
        element = self.driver.find_element(By.CSS_SELECTOR, ".\\_2hNaj")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # Click "Already have an account"
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"have-account\"]").click()
        time.sleep(3)

    def provide_credentials(self):
        # Provide the credentials
        #input("next? - credentials")
        l = credentials.get_login()
        print("l = " + str(l))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"email-input\"]").send_keys(l)

        #input("next? - credentials")
        p = credentials.get_password()
        print("p = " + str(p))
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password-input\"]").send_keys(p)
        #input("next? - credentials")
        time.sleep(1)

    def click_login(self):
        # Click "Login"
        #input("next? - login")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"register-button\"]").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3ryeM")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(6)
        input("Have you logged in successfully?")


    def __from_11_to_2(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(11)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()

    def __from_9_to_2(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(9)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()
        
    def switch_to_french(self):
        # Title: "Duolingo - The world's best way to learn......"
        if 'French' in self.driver.title:
            pass
        elif 'Chinese' in self.driver.title:
            self.__from_9_to_2()
        else: 
            input("error!")

    def switch_to_stories(self):
        # Switch to the "Stories"
        #input("next? - to stories")
        element = self.driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(3) .\\_1KHTi")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(3) .\\_1KHTi").click()
        time.sleep(3)

    def start_the_story(self):        
        # Scroll to y=1 line
        # input("next? - scroll to the beginning of the page")
        self.driver.execute_script("window.scrollTo(0,1)")
        time.sleep(1)

        # Start the first story
        # input("next? - start the first story")
        self.driver.find_element(By.CSS_SELECTOR, ".set:nth-child(2) > .story:nth-child(3) .story-cover-illustration-image").click()

    def click_continue(self,t=0.5):
        time.sleep(t)
        print('continue')
        self.driver.find_element_by_class_name("continue").click()        

    def pick_li_answer(self, answer):
        i=1
        while(1):
            e = self.driver.find_element_by_class_name("challenge-answers li:nth-of-type("+str(i)+")")
            if e.text == answer:
                e.click()
                break
            i = i+1
            if i > 3:
                print('ERROR: i>3 in pick_'+answer)
            #input("next?")  
            time.sleep(1)      

    def pick_6th_phrase(self):
        e = self.driver.find_element(By.CSS_SELECTOR, ".phrase:nth-child(6) .point-to-phrase-synced-text")
        if e.text != 'fatiguée':
            print('ERROR: fatiguee not found')
        else:
            e.click()


    def match_tokens(self):
        tokens = []
        tokens_matched = []
        for i in range(1,11):
            input("next? i = "+str(i))        
            e = driver.find_element_by_class_name("tokens li:nth-of-type("+str(i)+")")
            current_token = e.text
            if current_token in tokens:
                tokens.append(e.text+'_DUPLICATE')
            else:
                tokens.append(e.text)
        print(str(tokens))

        import story1
        d = story1.expand_dict(story1.dict)
        print(d)
        for j in range(len(tokens)):
            input('next?')
            t = tokens[j]
            print("token= " + t)
            if t in tokens_matched:
                continue

            t_match = d[t]
            print(t + " --> " + t_match)
            
            e_token = driver.find_element_by_class_name("tokens li:nth-of-type("+str(j+1)+")")
            print(e_token.text)
            e_token.click()

            if t == t_match:
                t_match = t_match+'_DUPLICATE'
                print('Modified t_match : ' + t_match)

            j_match = tokens.index(t_match)
            e_token_matched = driver.find_element_by_class_name("tokens li:nth-of-type("+str(j_match+1)+")")
            print(e_token_matched.text)
            e_token_matched.click()

            tokens_matched.append(t)
            tokens_matched.append(t_match)


    def click_continue_skip(self):
        time.sleep(0.5)
        print('continue')
        self.driver.find_element_by_class_name("skip").click()        







    def the_rest(self):

        # Choose a word
        element = self.driver.find_element(By.CSS_SELECTOR, ".phrase:nth-child(6) .point-to-phrase-synced-text")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".phrase:nth-child(6) .point-to-phrase-synced-text").click()
       # a PAUSE here to listen "Marion mets du sucre dans sa tasse"

        # 
        self.driver.find_element_by_class_name("continue").click()

        # Choose a checkbox "She put sugar in her coffee"
        element = self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button").click()

        # 
        self.driver.find_element_by_class_name("continue").click()
        self.driver.find_element_by_class_name("continue").click()
        self.driver.find_element_by_class_name("continue").click()
        self.driver.find_element_by_class_name("continue").click()

        # Choose a checkbox for "quoi = What?"
        element = self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(1) > button").click()

        # 
        self.driver.find_element_by_class_name("continue").click()
        self.driver.find_element_by_class_name("continue").click()
        self.driver.find_element_by_class_name("continue").click()

        # Choose a checkbox "Marion was so tired that shee... put solt in her coffee"
        element = self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".click-to-select:nth-child(3) > button").click()

        # 
        self.driver.find_element_by_class_name("continue").click()

        # Match the words.......
        #
        #
        #

        # 
        self.driver.find_element_by_class_name("continue").click() # Done
        self.driver.find_element_by_class_name("continue").click() # You earned 24 XP
        self.driver.find_element_by_class_name("continue").click() # Story complete!
        self.driver.find_element_by_class_name("continue").click() # Back to "Stories"


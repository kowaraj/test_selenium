
# 15 | mouseOver | css=.v836l:nth-child(11) |  | 
element = driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(11)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 16 | click | css=.\_2-Lx6 > .U_ned:nth-child(2) |  | 
driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()

# 17 | mouseOver | css=.v836l:nth-child(9) |  | 
element = driver.find_element(By.CSS_SELECTOR, ".v836l:nth-child(9)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 18 | click | css=.\_2-Lx6 > .U_ned:nth-child(2) |  | 
driver.find_element(By.CSS_SELECTOR, ".\\_2-Lx6 > .U_ned:nth-child(2)").click()
  

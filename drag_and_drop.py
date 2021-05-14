import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\shilp\\Downloads\\UFT_One_15.0_DVD\\Unified Functional Testing\\MSI\\Micro Focus\\Unified Functional Testing\\bin\\WebDriver\\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)
fromelement = driver.find_element_by_id("draggable")
toelement = driver.find_element_by_id("droppable")
time.sleep(2)
try:
    actions = ActionChains(driver)
    # There are two ways to use drag and drop
    #actions.drag_and_drop(fromelement, toelement).perform()
    actions.click_and_hold(fromelement).move_to_element(toelement).release().perform()
    print("Drag and drop successful")
    time.sleep(2)
    destinationfile = 'C:/Users/shilp/Desktop/Test1.png'
    driver.save_screenshot(destinationfile)

except:
    print("Drag and drop not done")
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
driver.get(url)
print("Page loaded.")

#execute javascript to scroll
driver.execute_script("window.scrollTo(0, 250)")

#using driver to click on dropdown
driver.find_element_by_xpath("//select[@name='continents']").click()

#identify dropdown with Select class
sel = Select(driver.find_element_by_xpath("//select[@name='continents']"))
#select by select_by_visible_text() method
sleep(2)
sel.select_by_visible_text("Africa")
sleep(2)
#select by select_by_index() method
sel.select_by_index(0)
sleep(2)

driver.close()
print("Finished.")
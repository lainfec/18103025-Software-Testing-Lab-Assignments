from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
  
url='https://pec.ac.in/'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
print ("Opened PEC homepage")
sleep(1)

page_title = driver.title

sleep(5)

driver.quit()
print("Page title is - ", page_title)
print("Finished")

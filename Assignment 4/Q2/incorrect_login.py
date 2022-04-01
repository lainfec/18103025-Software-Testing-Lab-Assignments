from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
  
usr='thalesdesu@gmail.com' 
pwd='TotallyIncorrectPassword'
url='https://www.facebook.com/'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
print ("Opened facebook")
sleep(1)

input()
  
username_box = driver.find_element(by=By.ID, value = 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
  
password_box = driver.find_element(by=By.ID, value ='pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element(by=By.NAME, value ='login')
login_box.click()
  
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
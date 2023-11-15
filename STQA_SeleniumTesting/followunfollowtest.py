
import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome(ChromeDriverManager().install())

#driver.get('https://tweetercloneapp.netlify.app/signin')


driver.get('https://tweetercloneapp.netlify.app/')


email = ""
password = ""


loginField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[1]')

passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[2]')

loginButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/button')

loginField.send_keys(email)

passwordField.send_keys(password)

loginButton.click()

time.sleep(2)


wait = WebDriverWait(driver, 7)  

print("<------- Test Case 27--Follow------->\n")

followButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/section/section[1]/div/button')))
followButton.click()

print("Test Case 27 run successfully!!\n")

time.sleep(3)

print("<------- Test Case 28--Unfollow------->\n")

followButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/section/section[1]/div/button')))
followButton.click()

print("Test Case 28 run successfully!!\n")

time.sleep(3)
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


wait = WebDriverWait(driver, 4)  
tweetInputField = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/div/div[1]/div/textarea')))

#tweetInputField = driver.find_element_by_xpath(
#    '/html/body/div/div/div/main/div[1]/div')
print("<------- Test Case 17--Tweet Input------->\n")


tweet = "Hello Twitter!"

tweetInputField.send_keys(tweet)

time.sleep(3)

tweetButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/main/div[1]/div/div[2]/button')

print("Test Case 17 run successfully!!\n")

print("<------- Test Case 18--Tweet ------->\n")


time.sleep(1)
tweetButton.click()

print("Test Case 18 Pass!! Tweeted Successfully\n")
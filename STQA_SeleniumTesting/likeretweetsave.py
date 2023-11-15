
import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome(ChromeDriverManager().install())


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

###### LIKE RETWEET SAVE###### 

print("<------- Test Case 21--Like Tweet------->\n")

likeButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[3]/span[1]')))
likeButton.click()

print("Test Case 21 run successfully!!")

time.sleep(2)

print("<------- Test Case 22--ReTweet------->")

retweetButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[2]/span[1]')))
retweetButton.click()

print("Test Case 22 run successfully!!")

time.sleep(3)

print("<------- Test Case 23--Save Tweet------->")

saveButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[4]/span[1]')))
saveButton.click()

print("Test Case 23 run successfully!!")

time.sleep(1)


###### UNLIKE UNDO-RETWEET UNSAVE######

print("<------- Test Case 24--Unlike Tweet------->")

likeButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[3]/span[1]')))
likeButton.click()

print("Test Case 24 run successfully!!")

time.sleep(2)

print("<------- Test Case 25--Undo ReTweet------->\n")

retweetButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[2]/span[1]')))
retweetButton.click()

print("Test Case 25 run successfully!!\n")

time.sleep(3)

print("<------- Test Case 26--Unsave Tweet ------->\n")

saveButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[1]/section/article[1]/div[2]/a[4]/span[1]')))
saveButton.click()

print("Test Case 26 run successfully!!\n")

time.sleep(1)

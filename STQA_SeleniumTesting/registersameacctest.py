from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://tweetercloneapp.netlify.app/signup')


email = ""
password = ""

emailField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[1]')

passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[2]')

signupButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/button')

emailField.send_keys(email)

passwordField.send_keys(password)

print("TestCase16..")
signupButton.click()
print("TestCase16 run successfully!!")
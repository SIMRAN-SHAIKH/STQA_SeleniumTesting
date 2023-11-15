from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://tweetercloneapp.netlify.app/signin')

email = ""
password = "" #Provide wrong password

loginField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[1]')

passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[2]')

loginButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/button')


loginField.send_keys(email)

passwordField.send_keys(password)

print("TestCase8.. Input Wrong Password or UserId")
loginButton.click()
print("TestCase8 run successfully!!   Login Failed!")
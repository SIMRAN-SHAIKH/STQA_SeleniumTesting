from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

print("TestCase1.. Open Login Page\n")

driver.get('https://tweetercloneapp.netlify.app/signin')

print('testcase1 run successfully!!\n')

email = "" #Provide mail address here and specify in all test cases
password = "" #Provide Password

print("TestCase2.. Input in Login Field\n")
loginField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[1]')

print("TestCase2 run successfully!!\n")

print("TestCase3.. Input in Password Field\n")

passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[2]\n')

print("TestCase3 run successfully!!\n")

print("TestCase4.. Login Button Working")

loginButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/button\n')

print("TestCase4 run successfully!!\n")

print("TestCase5.. Input UserId")
loginField.send_keys(email)
print("TestCase5 run successfully!!\n")

print("TestCase6.. Enter Password\n")
passwordField.send_keys(password)
print("TestCase6 run successfully!!\n")

print("TestCase7..Login Account\n")
loginButton.click()
print("TestCase7 run successfully   Login Successful!!\n")


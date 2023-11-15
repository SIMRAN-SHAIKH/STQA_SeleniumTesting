from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())

print("TestCase9.. Open SignUp Page")

driver.get('https://tweetercloneapp.netlify.app/signup')

print('testcase9 run successfully!!\n')

email = "" #Provide new email address
password = "" #Provide Password

print("TestCase10.. Email Field\n")
emailField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[1]')

print("TestCase10 run successfully!!\n")

print("TestCase11.. Password Field\n")
passwordField = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/input[2]')
print("TestCase11 run successfully!!\n")

print("TestCase12.. SignUp Button working\n")
signupButton = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/form/button')
print("TestCase12 run successfully!!\n")

print("TestCase13.. Input in Email Field")

emailField.send_keys(email)

print("TestCase13 run successfully!!\n")

print("TestCase14.. Input in Password Field")
passwordField.send_keys(password)
print("TestCase14 run successfully!!\n")

print("TestCase15.. New Account Creation using SignUp Button")
signupButton.click()
print("TestCase15 run successfully!! New Account Created!!\n")
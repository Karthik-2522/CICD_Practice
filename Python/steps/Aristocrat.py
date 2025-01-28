import  selenium
from    selenium import  webdriver 
from    selenium.webdriver.common.by import  By 
from    selenium.webdriver.common.keys import Keys 
from    behave import Given, When, Then
import  os
from    selenium.webdriver.support.ui import WebDriverWait
from    selenium.webdriver.support  import  expected_conditions as EC


@Given('I am on the Demo Login Page')
def Login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
@When('I fill the account information for account standardUser into the Username field and Password field')
def fill_Valid_credentials(context):
    username = context.driver.find_element(By.ID,'user-name')
    username.send_keys("standard_user")
    password = context.driver.find_element(By.ID,'password')
    password.send_keys("secret_sauce")
@When('I click the Login Button')
def click_login_button(context):
    login_button = context.driver.find_element(By.ID,'login-button').click()
@Then('I am redirected to the Demo Main Page')
def redirect_to_main_page(context):
    context.driver.find_element(By.XPATH,".//div[text()='Swag Labs']")
    print("User logged into the Mainpage")
    screenshot = 'screenshot'
    os.makedirs(screenshot,exist_ok=True)
    screenshot_path = os.path.join(screenshot,'validlogin.png')
    context.driver.get_screenshot_as_file(screenshot_path)
@Then('I Verify the App Logo exists')
def verifiy_app_logo(context):
    try:
        context.driver.find_element(By.XPATH,".//div[text()='Swag Labs']")
        print("User logged into the Mainpage")
    except:
        print("User Not Logged in Successfully")
        screenshot = 'screenshot'
        os.makedirs(screenshot,exist_ok=True)
        screenshot_path = os.path.join(screenshot,'Invalidlogin.png')
        context.driver.get_screenshot_as_file(screenshot_path)
@When('I fill the account information for account LockedOutUser into the Username field and Password field')
def fill_Invalid_credentials(context):
    username = context.driver.find_element(By.ID,'user-name')
    username.send_keys("locked_out_user")
    password = context.driver.find_element(By.ID,'password')
    password.send_keys("secret_sauce")
@Then('I Verifiy the Error Message Contains the text "Sorry, this user has been banned. "')
def verify_error_message(context):
    erro_msg_act = context.driver.find_element(By.TAG_NAME,'h3').text
    screenshot = 'screenshot'
    os.makedirs(screenshot,exist_ok=True)
    screenshot_path = os.path.join(screenshot,'errormessage.png')
    context.driver.get_screenshot_as_file(screenshot_path)
    if erro_msg_act=='Epic sadface: Sorry, this user has been locked out.':
        print(f'user not login successfully and error message {erro_msg_act} shown')
    else:
        print('Testcase Fail')
@Given ('I am logged in')
def Navigate_to_loginpage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    username = context.driver.find_element(By.ID,'user-name')
    username.send_keys("standard_user")
    password = context.driver.find_element(By.ID,'password')
    password.send_keys("secret_sauce")
    login_button = context.driver.find_element(By.ID,'login-button').click()
@When('I am on the inventory page')
def Navigate_to_inventorypage(context):
    context.driver.find_element(By.XPATH,".//div[text()='Swag Labs']")
    screenshot = 'screenshot'
    os.makedirs(screenshot,exist_ok=True)
    screenshot_path = os.path.join(screenshot,'inventorypage.png')
    context.driver.get_screenshot_as_file(screenshot_path)
@Then('I extract content from the web page')
def extract_text(context):
    context.logo = context.driver.find_element(By.XPATH,".//div[text()='Swag Labs']").text
    # context.text = context.driver.find_element(By.XPATH,".//*[contains(@id,'inventory_container')]//div[contains(@class,'inventory_item_name ')]").text
@Then('Save it to a text file')
def extract_text(context):
    with open('Aristocrat.txt','w') as file:
        file.write(context.logo)
@Then('I log out')
def log_out(context):
    element = WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,".//*[contains(@id,'react-burger-menu-btn')]")))
    context.driver.find_element(By.XPATH,".//*[contains(@id,'react-burger-menu-btn')]").click()
    logout_btn = WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,".//*[contains(@id,'logout_sidebar_link')]")))
    context.driver.find_element(By.XPATH,".//*[contains(@id,'logout_sidebar_link')]").click()
@Then('I verify I am on the Login page again')
def loginpage_verfication(context):
    try:
        context.driver.find_element(By.ID,'login-button')
        print("User in Login Page")
        screenshot = 'screenshot'
        os.makedirs(screenshot,exist_ok=True)
        screenshot_path = os.path.join(screenshot,'loginpage.png')
        context.driver.get_screenshot_as_file(screenshot_path)
    except:
        print("Testcase Failed")


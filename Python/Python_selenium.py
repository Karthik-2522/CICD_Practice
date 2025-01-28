from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class testrun():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def initialize(self):
        self.driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
    def input_text(self,label_name,data):
         xpath = f".//span[normalize-space(text())='{label_name}']//parent::div//child::input"
        xpath = """.//span[normalize-space(text())=\""""+label_name+"\"]//parent::div//child::input"
        print(xpath)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
        self.driver.find_element(By.XPATH,xpath).send_keys("data")
        print("Pass")
        
        
a=testrun()
a.initialize()
a.input_text('First name:','Karthik')

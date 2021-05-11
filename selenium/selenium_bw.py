#################     import module     #################

# selenium lib
from selenium import webdriver
# from seleniumwire import webdriver                                                              # for receive response
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# time lib
from time import sleep
import util

class Driver: 
    def __init__(self):
        options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications" : 2}                      # disable alert part
        # options.add_experimental_option("prefs",prefs)                                            # disable alert part
        # options.add_argument("--headless")  
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--ignore-certificate-errors')                                     #disable ssl handshake err
        # options.add_argument('--ignore-ssl-errors')          #disable ssl handshake err
        options.add_experimental_option("excludeSwitches", ['enable-automation'])               # hide chrome is being contrlled
        # options.add_experimental_option("excludeSwitches", ["enable-logging"])                  # hide Getting Bluetooth err 
        # options.add_argument('--proxy-server=%s' % proxy) #set proxy                            # set proxy
        # options.add_argument(
        #     "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
        # options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
        # webdriver.DesiredCapabilities.CHROME['proxy']={
        #     "httpProxy":proxy,
        #     "ftpProxy":proxy,
        #     "sslProxy":proxy,
        #     "proxyType":"MANUAL",
        # }
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def __call__(self):
        return self.driver

    def get_url(self, url): 
        self.driver.get(url)

    def get_default(self):  
        while True:
            try:
                self.driver.switch_to.default_content()
                return
            except:
                print('default move frame')
                pass

    def get_fra(self, name):  
        while True:
            try:
                self.driver.switch_to.frame(name)
                break
            except:
                self.get_default()
                print(name, 'move frame')
                continue

    def find_by_id(self, id): 
        return WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located(
                 (By.ID, id)))

    def find_by_xpath(self, xpath): 
        return WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located(
                 (By.XPATH, xpath)))

    def find_by_class(self, class_name): 
        return WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located(
                 (By.CLASS_NAME, class_name)))

    def find_by_selector(self, class_name): 
        return WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located(
                 (By.CSS_SELECTOR, class_name)))

    def find_by_tag(self, tag): 
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, tag)))

    def find_by_name(self, name): 
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, name)))

    def find_all_by_class(self, class_name): 
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, class_name)))

    def find_all_by_tag(self, tag): 
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, tag)))

    def find_all_by_name(self, name): 
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.NAME, name)))

    def find_all_by_tag_with_obj(self, obj, name): 
        return WebDriverWait(obj, 20).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, name)))

    def find_by_tag_with_obj(self, obj, name): 
        return WebDriverWait(obj, 20).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, name)))

    def find_by_link(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, text)))

    def switch_to(self, str):
        self.driver.switch_to.frame(str)

    def execute_script(self, str):
        self.driver.execute_script(str)
        
    def full_screenshot(self):
        util.fullpage_screenshot(self.driver, "test.png")
        
    def click(self, btn):
        self.driver.execute_script("arguments[0].click();", btn)

    def close(self):
        self.driver.close()

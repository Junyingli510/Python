#################     Features     #################
# 1. Read the link list file and get links
# 2. Each 3~4 min viste random links
# 3. Each 30~45 min change user agent and ip address

#################     import module     #################

# selenium lib
# from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# proxy lib
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from proxyscrape import create_collector, get_collector

# request lib
import requests

# thread lib
from threading import Timer as thTimer
import schedule

# time lib
from time import sleep

# random lib
import random


class FileIO:
    def readfile(self, path):
        result = []
        f = open(path, 'r', encoding='utf8')
        rdd = f.readlines()
        for line in rdd:
            result.append(line)
        f.close()
        return result

    def writefile(self, path, type, data,):
        f = open(path, type, encoding='utf-8', newline='')
        wrd = f.readlines()
        # header = ['Name','Given Name']
        # wr.writerow(header)
        for i in data:
            for j in i:
                wrd.writerow([j])
        f.close()

class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}    # disable alert part
        options.add_experimental_option("prefs",prefs)                          # disable alert part
        # options.add_argument('headless')
        # options.add_argument(
        #     "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
        # options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def __call__(self):
        return self.driver

    def get_url(self, url): 
        self.driver.get(url)

    def get_default(self):  
        while True:
            try:
                self.driver.switch_to_default_content()
                return
            except:
                print('default move frame')
                pass

    def get_fra(self, name):  
        while True:
            try:
                self.driver.switch_to_frame(name)
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

    def click(self, btn):
        self.driver.execute_script("arguments[0].click();", btn)

    def close(self):
        self.driver.close()

ary_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
]
# no 85 74 87
# ok 84 72 89 63 21 60
FileIoClass = FileIO()

def randomUrl(list):
    choiceItem = random.choice(list)
    return choiceItem

def get_url():
    ary_link = FileIoClass.readfile('./Urls.txt')
    url = randomUrl(ary_link)
    print("_____ url " + url)
    return url

def get_connect_info():
    connect_info = {}
    agent = randomUrl(ary_agent)
    connect_info['agent'] = agent

    ################  free proxy  ################
    try:
        req_proxy = RequestProxy()
        print('Set proxy setting')
        proxies = req_proxy.get_proxy_list()
        print('Get proxy list')
    except:
        print('Proxy list is empty')
        pSleep(10)
        main()

    proxy_info = randomUrl(proxies)
    while proxy_info == "":  
        proxy_info = randomUrl(proxies)

    print('_____________  ' + str(proxy_info))
    try:
        proxy = proxy_info.get_address()
    except:
        proxy = proxy_info.split("|")[0]
    print('_____________  ' + str(proxy))
    connect_info['proxy'] = proxy
    ################  collect special country proxy  ################
    # for i in proxies:
    #     print(i)
    # for i in proxies:
    #     country = i.country
    #     # print(country)
    #     #  or country == 'Poland' or country == 'India' or country == 'Japan' or country == 'United Kingdom'
    #     if country == 'Korea' or country == 'Japan':
    #         connect_info['proxy'] = i.get_address()
    #         connect_info['proxy_country'] = i.country
    #         break

    ################  paid proxy  ################

    # proxeis_list_url = "http://filefab.com/api.php?l=CH-p20KmF9cekOALwRvOaGoIar3tEymzv3w68-e-HKc"
    # req_proxy = requests.get(proxeis_list_url)
        
    # proxies = req_proxy.text.split('\n')
    # print('_____ res list' + req_proxy.text)
    # proxy = randomUrl(proxies)
    # print('_____ res proxy ' + proxy + ' 1')
    # while proxy == "":  
    #     proxy = randomUrl(proxies)
    #     print('_____ res proxy ' + proxy + ' 2')

    # print('_____ res proxy ' + proxy + ' 3')
    # connect_info['proxy'] = proxy

    
    sleep(1)
    return connect_info

def change_agent_ip():
    connect_info = get_connect_info()
    agent = connect_info['agent']
    print("_____ agent " + agent)

    proxy = connect_info['proxy']
    print("_____ proxy " + proxy + ' !')

    # proxy_country = connect_info['proxy_country']
    # print("_____ country " + proxy_country)

    chrome_options = Options()  
    # chrome_options.add_argument("--headless")  
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # chrome_options.add_argument('--proxy-server=%s' % proxy)
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
    # chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
    # webdriver.DesiredCapabilities.CHROME['proxy']={
    #     "httpProxy":proxy,
    #     "ftpProxy":proxy,
    #     "sslProxy":proxy,
    #     "proxyType":"MANUAL",
    # }
    # agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
    # agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    agent_param = {}
    agent_param["userAgent"] = agent
    # print("_____ agent " + str(agent_param))
   
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True 
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
    # print(driver.execute_script("return navigator.userAgent;"))
    # Setting user agent 
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', agent_param)
    # print(driver.execute_script("return navigator.userAgent;"))
   
    return driver

def visit_url(driver):
    url = get_url()
    try:
        # test URL
        # driver.get("http://ip.json-json.com/")
        # driver.get("http://www.myipaddress.com/")
        # driver.get("https://nordvpn.com/what-is-my-ip/")
        # driver.get("https://api.myip.com/")

        # open main url and close ad
        pSleep(3)
        driver.get('https://aioz.tube/')
        # try:
        #     driver.get('https://aioz.tube/')
        #     pSleep(3)
        # except:
        #     driver.get('https://aioz.tube/')
        
        pSleep(5)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/button').click()
        pSleep(5)
        # run url
        driver.get(url)
        pSleep(5)
    
        # play video
        try:
            driver.find_element_by_xpath('//*[@id="player"]/button').click()
            pSleep(5)
        except :
            try:
                driver.find_element_by_xpath('//*[@id="player"]/button').click()
                pSleep(5)
            except:
                print("_____ get play video err ")
                print("_____ _____ _____ change proxy and agent")
                pSleep(2)
                driver.close()
                pSleep(2)
                driver.quit()
                main()
    except:
        print("_____ get url err ")
        print("_____ _____ _____ change proxy and agent")
        driver.close()
        pSleep(2)
        driver.quit()
        pSleep(2)
        main()

def pSleep(n):
    for i in range(1, n+1):
        print(i)
        sleep(1)

# every 3 min visit url
# every 30~45 min change agent and ip address
def main():
    unit = 60
    visit_sec = 3*unit + round(random.random()*unit)
    change_ip_sec = 30*unit + round(random.randrange(1, 15)*unit)

    visit_sec = 10
    change_ip_sec = 20
    print("_____ start main " + str(visit_sec) + ' ' + str(change_ip_sec))
    driver = change_agent_ip()
    call_count = round(change_ip_sec/visit_sec)
    
    for i in range(0, call_count):
        print('_____ call count ' + str(i+1)+ "/" + str(call_count))
        visit_url(driver)
        pSleep(visit_sec)

    # visit_url(driver)
    # pSleep(visit_sec)
    driver.close()
    pSleep(2)
    driver.quit()
    pSleep(2)
    thTimer(5, main).start()

   
if __name__ == '__main__':
    main()




#################     driver test     #################
# connect_info = get_connect_info()
# agent = connect_info['agent']
# print("_____ agent " + agent)

# proxy = connect_info['proxy']
# print("_____ proxy " + proxy + ' !')

# proxy_country = connect_info['proxy_country']
# print("_____ country " + proxy_country)

# chrome_options = Options()  
# # chrome_options.add_argument("--headless")  
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')  #disable ssl handshake err
# chrome_options.add_argument('--ignore-ssl-errors')          #disable ssl handshake err
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # hide chrome is being contrlled
# # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])   # hide Getting Default Adapter failed.
# chrome_options.add_argument('--proxy-server=%s' % proxy) #set proxy
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
# # chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
# # webdriver.DesiredCapabilities.CHROME['proxy']={
# #     "httpProxy":proxy,
# #     "ftpProxy":proxy,
# #     "sslProxy":proxy,
# #     "proxyType":"MANUAL",
# # }
# # agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
# # agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
# agent_param = {}
# agent_param["userAgent"] = agent
# # print("_____ agent " + str(agent_param))

# driver = webdriver.Chrome(executable_path=r'C:\\chromedriver\\chromedriver.exe', options=chrome_options)
# print(driver.execute_script("return navigator.userAgent;"))

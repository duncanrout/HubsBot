import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

#from selenium import webdriver
options = uc.ChromeOptions()

def RandomWait():
    time.sleep(1 + random.random()*2)

def signIn():
    ##profile work
    #options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    ##profile home
    options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"


signIn()

options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    driver.get('https://napat.sales-i.com/Accounts')   
    home_window = driver.window_handles[0]
    print(home_window)
    time.sleep(30)
    home_window = driver.window_handles[0]
    print(home_window)
    driver.find_element_by_xpath("/html/body/app-root/app-accounts/div[2]/app-search/div/div[1]/div/div[4]/div[1]/p-checkbox/div/div[2]/span").click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/app-root/app-accounts/div[2]/app-search/div/div[1]/div/div[1]/button").click()
    
    #deselect customers
    #hit search
    #open all tabs
    #Look at first row and look at City state zip tele email...
    #Also pull the Data added. (Name, city... Date added)

        #If( Name contains 'Admin' ) mark as do not delete
        #elif( columns are empty or data added <= 2019) mark as delete
        #else mark as do not delete

    #move onto next and repeat

    #once finished, check to see if names account num match and delete
    #move onto next section

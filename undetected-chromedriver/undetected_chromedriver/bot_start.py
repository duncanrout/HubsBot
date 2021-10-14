
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
def toAccountsPage():
    #clicky click click... Using coworker's login since mine isn't activated
    driver.get('https://napat.sales-i.com/Accounts')   
    home_window = driver.window_handles[0]
    driver.find_element_by_xpath("//*[@id='main-btn']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='main-btn']").click()
    driver.find_element_by_xpath("//*[@id='ClientId']").click()
    #Picking Chicago
    driver.find_element_by_xpath("//*[@id='ClientId']/option[17]").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/form/div[2]/input").click()   
    driver.find_element_by_xpath("//*[@id='view-as-select']").click()
    #Picking Victor
    driver.find_element_by_xpath("//*[@id='view-as-select']/option[63]").click()
    driver.find_element_by_xpath("//*[@id='view-as-form']/div[1]/a").click()
    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div/div/iframe"))
    driver.find_element_by_xpath("/html/body/app-root/app-accounts/div[2]/app-search/div/div[1]/div/div[3]/div[1]/p-checkbox/div").click()
    driver.find_element_by_xpath("/html/body/app-root/app-accounts/div[2]/app-search/div/div[1]/div/div[1]/button").click()
    
signIn()

options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
driver.implicitly_wait(6)

with driver:

    toAccountsPage()

    #Iterate()
    xpathOriginal = "//*[@id='accounts']/div/div[1]/div/div[2]/table/tbody/tr[1]/td[1]"

    for y in range(101):
        currentNumY = str(y+1)
        xpathCurrent = xpathOriginal[0:57] + currentNumY + xpathOriginal[58:]
        print("Row " + str(y))
        
        for x in range(9):
            
            currentNumX = str(x+1)
            if (y >= 9):
                xpathCurrent = xpathCurrent[0:64] + currentNumX + xpathCurrent[65:]
            else:
                xpathCurrent = xpathCurrent[0:63] + currentNumX + xpathCurrent[64:]
        
            currentBox = driver.find_element_by_xpath(xpathCurrent).text
            if(not currentBox):
                print("Empty!")
            else:
                print(currentBox)

    
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

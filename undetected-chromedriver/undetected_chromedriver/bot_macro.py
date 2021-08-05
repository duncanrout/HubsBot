import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium import webdriver
options = uc.ChromeOptions()

def signIn():
    ##profile work
    options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    ##profile home
    #options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

#opens the first 25 domain links - driver must point to homepage
def Open25Windows():
    xpathOriginal = "/html/body/div[2]/div[1]/div/div[2]/div/div/section/div/div/main/div/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/a"
    for x in range(25):
        currentNum = str(x+1)
        xpathCurrent = xpathOriginal[0:117] + currentNum + xpathOriginal[117+1:]
        print(xpathCurrent)
        driver.find_element_by_xpath(xpathCurrent).click()


#Bot Start
signIn()

#just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    #open home page
    driver.get('https://app.hubspot.com/contacts/1734343/objects/0-2/views/6117919/list')
    driver.implicitly_wait(2)

    print("test2")
          
    home_window = driver.window_handles[0]
    Open25Windows()
    driver.implicitly_wait(5)
    handles = driver.window_handles
    size = len(handles)
    
    print("test3")
    
    for x in reversed(range(25)):
        try:
            driver.switch_to.window(handles[x+1])
            driver.find_element_by_id("ro__button_unminimize_container").click()
            driver.implicitly_wait(2)
            print(driver.title)
        except:
            print("Unable to open window or box")

    driver.switch_to.window(home_window)
    print("Finished!")
                                           
        
    
                                                                
    

import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random 

#from selenium import webdriver
options = uc.ChromeOptions()

fit = False
unsureFit = False
fitTrack = []


def RandomWait():
    time.sleep(random.random()*2)

def signIn():
    ##profile work
    options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    ##profile home
    #options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
   

#Not used
def employeeTrack():
    #Once at Company IFrame
    driver.find_element_by_xpath("//*[@id='Employees-']/div/div").click()
    try:
        driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-profile-wrapper/zi-profile-content-v2/div/div[2]/zi-company-employees/zi-row-secondary-content/div/zi-management-role-chip/span/span/span[1]/div/a/span/div[1]").click()

    except:
        print("try again")


    #driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container-v2/div/div/div[1]/zi-filters-ng/div/div/div[2]/zi-shared-filters-container-ng/div[1]/div[2]/div/span").click()
    #//*[@id="job-titles-filters"]/div/span
    #//*[@id="jobFunctions-Sales"]/label/span[1]
    #//*[@id="people-search"]/span
        #^.text


    print(sales_reps)


def AnalyseWebsite():
    fit = False
    unsureFit = False
    employeeDrop = True
    try:
        #Finding Revenue : TODO: (Pull revenue from different source)
        RandomWait()
        driver.find_element_by_id("ro__button_unminimize_container").click()
        RandomWait()
        driver.switch_to.frame(driver.find_element_by_id("ro__extension_iframe"))
        RandomWait()
        driver.switch_to.frame(driver.find_element_by_id("GrowIframe"))
        RandomWait()
        revenue = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/zi-reachout-tabs/div[2]/zi-reachout-company-detail-tab/zi-reachout-company-data-tab/div/div/zi-reachout-company-detail/div/div[6]/span").text
        #print(revenue)
        revCheck = False
        repCheck = False
        billion = False
        million = False
        if('B' in revenue):
            billion = True
        elif('M' in revenue):
            million = True
        else:
            revCheck = False
        if(billion):
            revCheck = True
        if(million):
            revenue = revenue[1:3]
            if(revenue.isspace()):
                revenue = revenue[1:]
            if(revenue.isspace()):
                revenue = revenue[1:]
            revenue = int(revenue)
            #print(revenue)
        if(revenue > 12 or billion):
            revCheck = True
            #print("Has enough Revenue")
        else:
            revCheck = False
            #print("Not enough Revenue")
        #Finding Sales Reps
        driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/div/zi-reachout-company-header/div/div[2]/div[1]").click()
        RandomWait()
        #employeeTrack()
        #time.sleep(20)
        driver.find_element_by_xpath("//*[@id='Org-Chart-']/div").click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath("//*[@id='departments-dropdown']/i").click()
            RandomWait()
            driver.find_element_by_xpath("//*[@id='selected-item-Sales']").click()
            RandomWait()
            driver.find_element_by_xpath("//*[@id='false']/label/span[1]").click()
            RandomWait()
            reps = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-profile-wrapper/zi-profile-content-v2/div/div[2]/zi-company-org-chart/div/zi-org-charts/div/div[1]/div[1]/zi-select-manager/zi-dropdown/div/span").text
            #print(reps)
            reps = reps[:2]
            #print(reps)
            if(not reps.isalpha()):
                reps = int(reps)
                if(reps > 3):
                    repCheck = True
                    #print("Has enough Reps")
                else:
                    repCheck = False
                    #print("Not enough Reps")
            if(repCheck and revCheck):
                fit = True
            else:
                fit = False     
        except:
            employeeDrop = False
            fit = False          
    except:
        unsureFit = True
        fit = False

    if(fit):
        fitTrack.append(1)
        print("Could be a fit!")
    elif(unsureFit):
        print("No ZI button or something went wrong, not sure if fit")
        fitTrack.append(5)
    else:
        if(employeeDrop == False):
            print("No employee dropdown, not a fit")
        else:
            print("Considered not a fit")
        fitTrack.append(0)

#Bot Start
signIn()


#just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
driver.implicitly_wait(6)

with driver:
    #open home page
    driver.get('https://app.hubspot.com/contacts/1734343/objects/0-2/views/6117919/list')
    
          
    home_window = driver.window_handles[0]
    RandomWait()

    xpathOriginal = "/html/body/div[2]/div[1]/div/div[2]/div/div/section/div/div/main/div/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/a"
    for x in range(5):
        print(x+1)
        currentNum = str(x+1)
        xpathCurrent = xpathOriginal[0:117] + currentNum + xpathOriginal[117+1:]
        try:
            driver.find_element_by_xpath(xpathCurrent).click()
            p = driver.current_window_handle
            chwd = driver.window_handles
            for w in chwd:
                if(w!=p):
                    driver.switch_to.window(w)
            AnalyseWebsite()
        
            driver.close()
            driver.switch_to.window(home_window)
        except:
            print("something went wrong here")
            print(fitTrack)
    print(fitTrack)
    

    
                                                                
    

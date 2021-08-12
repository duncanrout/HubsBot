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
    time.sleep(1 + random.random()*3)

def signIn():
    ##profile work
    options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    ##profile home
    #options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
   

#Top Contacts Route
def EmployeesRoute():
    sreps = 0
    try:
        driver.find_element_by_xpath("//*[@id='Employees-']/div/div").click()
        driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-profile-wrapper/zi-profile-content-v2/div/div[2]/zi-company-employees/zi-row-secondary-content/div/zi-management-role-chip/span/span/span[1]/div/a/span/div[1]").click()
        RandomWait()
        driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container-v2/div/div/div[1]/zi-filters-ng/div/div/div[2]/zi-shared-filters-container-ng/div[1]/div[2]/div/span").click()
        RandomWait()
        driver.find_element_by_xpath("//*[@id='job-titles-filters']/div/span").click()
        RandomWait()
        driver.find_element_by_xpath("//*[@id='jobFunctions-Sales']/label/span[1]").click()
        RandomWait()
        sreps = driver.find_element_by_xpath("//*[@id='people-search']/span").text
        sreps = sreps[2:4]
        #does not account for 100+ sales reps... should be found by other track anyways

        if(")" in sreps):
            sreps = sreps[:1]
   
        print("Found the reps the other way! The company has " + sreps)
        sreps = int(sreps)
    except:
        print("No Employee Button available")
    return(sreps)
    

def AnalyseWebsite():
    fit = False
    unsureFit = False
    employeeDrop = True
    OrgChartRoute = True
    EmployeeRoute = True
    OpenZI = True
    revCheck = False
    repCheck = False
    foundReps = False
    reps = 0
    try:
        try:
            RandomWait()
            driver.find_element_by_id("ro__button_unminimize_container").click()
            RandomWait()
            driver.switch_to.frame(driver.find_element_by_id("ro__extension_iframe"))
            RandomWait()
            driver.switch_to.frame(driver.find_element_by_id("GrowIframe"))
            RandomWait()
            revenue = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/zi-reachout-tabs/div[2]/zi-reachout-company-detail-tab/zi-reachout-company-data-tab/div/div/zi-reachout-company-detail/div/div[6]/span").text
            billion = False
            million = False
            if('B' in revenue):
                billion = True
                print("This company has a revanue of billion or more")
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
                print("Company has a revanue of $" + str(revenue) + " million")
            if(revenue > 12 or billion):
                revCheck = True
            else:
                revCheck = False
        except:
            print("Could not open ZI")
            OpenZI = False
            
        #If ZI was able to be opened
        if(OpenZI == True):
            #Open up ZI long
            driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/div/zi-reachout-company-header/div/div[2]/div[1]").click()
            RandomWait()
            try:
                driver.find_element_by_xpath("//*[@id='Org-Chart-']/div").click()
                time.sleep(5)
                try:
                    driver.find_element_by_xpath("//*[@id='departments-dropdown']/i").click()
                    RandomWait()
                    #Try to find the reps
                    try:
                        driver.find_element_by_xpath("//*[@id='selected-item-Sales']").click()
                        RandomWait()
                        driver.find_element_by_xpath("//*[@id='false']/label/span[1]").click()
                        RandomWait()
                        reps = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-profile-wrapper/zi-profile-content-v2/div/div[2]/zi-company-org-chart/div/zi-org-charts/div/div[1]/div[1]/zi-select-manager/zi-dropdown/div/span").text
                        reps = reps[:2]
                        print("Found it! The company has " + str(reps) + "sales rep/s")
                        reps = int(reps)
                        foundReps = True
                    except:
                        print("No sales option available, not a fit")
                        reps = 0
                except:
                    print("No Dropdown... Trying another way")
            except:
                print("No Org Chart Button available... Trying another way")
            if(foundReps == False):
                try:
                    reps = 0
                    #Try the Employees Route
                    reps = EmployeesRoute()
                except:
                    print("This did not work either")
        else:
            print("Unsure of fit... Something went wrong ex: no ZI or won't load")
            unsureFit = True
    except:
        print("Something went wrong")
        unsureFit = True

    #Final Checks
    #Check to see if reps is an int
    if((reps > 3) and revCheck):
        fit = True
    if(fit):  
        fitTrack.append(1)
        print("Could be a fit!")
    elif(unsureFit):
        fitTrack.append(5)
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
    for x in range(15):
        print("Company: " + str(x+1))
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
    

    
                                                                
    

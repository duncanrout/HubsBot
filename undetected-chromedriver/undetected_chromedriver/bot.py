import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium import webdriver
options = uc.ChromeOptions()

fit = False
unsureFit = True
fitTrack = []


def signIn():
    ##profile work
    options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    #profile home
    #options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
   

#Not used
def employeeTrack():
    #Once at Company IFrame
    driver.find_element_by_xpath("//*[@id='Employees-']/div/div").click()
    driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-search-result-row/zi-search-result-row/zi-profile-content/div/div[2]/zi-row-secondary-content/div/zi-management-role-chip/span/span/span[1]/div/a/span/div[1]/span/span").click()
    driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container/zi-page-template/div/div/zi-page-content/div/div/div[1]/zi-filters/div/div/div[2]/div/zi-shared-filters-container/div[1]/div/span").click()
    driver.find_element_by_xpath("//*[@id='job-titles-filters']/div/span").click()
    driver.find_element_by_xpath("//*[@id='jobFunctions-Sales']/label/span[1]").click()
    sales_reps = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container/zi-page-template/div/div/zi-page-content/div/div/div[2]/zi-people-results-page/div/div/div[2]/div/div[1]").text
    #sales_reps = driver.find_element_by_class_name("results-count")
    #sales_reps = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container/zi-page-template/div/div/zi-page-content/div/div/div[2]/zi-people-results-page/div/div/div[2]/div/div/span[1]")
    #Prints out black, realized it was wrong number anyways
    print(sales_reps)


def AnalyseWebsite():
    try:
        #Finding Revenue : TODO: (Pull revenue from different source)
        driver.find_element_by_id("ro__button_unminimize_container").click()
        
        driver.switch_to.frame(driver.find_element_by_id("ro__extension_iframe"))
        driver.switch_to.frame(driver.find_element_by_id("GrowIframe"))
        revenue = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/zi-reachout-tabs/div[2]/zi-reachout-company-detail-tab/zi-reachout-company-data-tab/div/div/zi-reachout-company-detail/div/div[6]/span").text
        revenue = revenue[1:4]
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
            revenue = revenue[1:4]
            if(revenue.isspace()):
                revenue = revenue[1:]
            if(revenue.isspace()):
                revenue = revenue[1:]
            revenue = int(revenue)
            if(revenue > 12):
                revCheck = True
                print("Has enough Revenue")
            else:
                revCheck = False
                print("Not enough Revenue")
        #Finding Sales Reps
        driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/div/zi-reachout-company-header/div/div[2]/div[1]").click()
        driver.find_element_by_xpath("//*[@id='Org-Chart-']/div").click()
        try:
            driver.find_element_by_xpath("//*[@id='departments-dropdown']/i").click()
            driver.find_element_by_xpath("//*[@id='selected-item-Sales']").click()
            driver.find_element_by_xpath("//*[@id='false']/label/span[1]").click()
            reps = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-profile-wrapper/zi-profile-content-v2/div/div[2]/zi-company-org-chart/div/zi-org-charts/div/div[1]/div[1]/zi-select-manager/zi-dropdown/div/span").text
            reps = reps[:1]
            reps = int(reps)
            if(reps > 4):
                repCheck = True
                print("Has enough Reps")
            else:
                print("Not enough Reps")

            if(repCheck and revCheck):
                unsureFit = True
                print("Could be a fit!")
            else:
                fit = False
                print("For sure not a fit...")
            
            
        except:
            print("No employee dropdown, likely not a fit")
            fit = False
            
            
    except:
        print("No zoominfo button, not sure if fit")
        fit = False

    if(fit):
        fitTrack.append(1)
    else:
        fitTrack.append(0)
    

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
driver.implicitly_wait(5)

with driver:
    #open home page
    driver.get('https://app.hubspot.com/contacts/1734343/objects/0-2/views/6117919/list')
          
    home_window = driver.window_handles[0]
    Open25Windows()
    handles = driver.window_handles
    size = len(handles)

    #iterate thru windows
    for x in reversed(range(25)):
        try:
            driver.switch_to.window(handles[x+1])
            AnalyseWebsite()
            print(driver.title)
        except:
            print("Unable to open window")
    
    print(fitTrack)

    driver.switch_to.window(home_window)

        
    
                                                                
    

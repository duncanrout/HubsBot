import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium import webdriver
options = uc.ChromeOptions()


def signIn():
    ##profile work
    #options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

    #profile home
    options.user_data_dir = "C:\\Users\\dunca\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    
signIn()

# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    #driver.get('https://app.hubspot.com/login/?hsCtaTracking=d82c5d82-821c-4c0d-86f5-6c34dced0e6d%7C16494015-d90f-47fc-adc3-593e2e1bdfa0')
    driver.get('https://app.hubspot.com/contacts/1734343/objects/0-2/views/5765433/list')
    driver.implicitly_wait(2)
    window_before_title = driver.title
    print(window_before_title)
    home_window = driver.window_handles[0]
    print(home_window)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/div/section/div/div/main/div/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/a").click()
    driver.implicitly_wait(2)
    window_after = driver.window_handles[1]
    print(window_after)
    driver.switch_to.window(window_after)
    window_after_title = driver.title
    print(window_after_title)

    #//*[@id="app-root"]/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/zi-reachout-tabs/div[2]/zi-reachout-company-detail-tab/zi-reachout-company-data-tab/div/div/zi-reachout-company-detail/div/div[5]/span

    driver.find_element_by_id("ro__button_unminimize_container").click()
    driver.implicitly_wait(2)
    driver.switch_to.frame(driver.find_element_by_id("ro__extension_iframe"))
    driver.implicitly_wait(2)
    driver.switch_to.frame(driver.find_element_by_id("GrowIframe"))
    revenue = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/zi-reachout-tabs/div[2]/zi-reachout-company-detail-tab/zi-reachout-company-data-tab/div/div/zi-reachout-company-detail/div/div[5]/span").text
    print(revenue)
    driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-reachout/div/div[2]/zi-reachout-company/div/section/div/div/zi-reachout-company-header/div/div[2]/div[1]").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//*[@id='Employees-']/div/div").click()
    #/div/div/span

    
    driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-profile-page/zi-page-template/div/div/zi-page-content/div/zi-company-search-result-row/zi-search-result-row/zi-profile-content/div/div[2]/zi-row-secondary-content/div/zi-management-role-chip/span/span/span[1]/div/a/span/div[1]/span/span").click()
    driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container/zi-page-template/div/div/zi-page-content/div/div/div[1]/zi-filters/div/div/div[2]/div/zi-shared-filters-container/div[1]/div/span").click()

    driver.find_element_by_xpath("//*[@id='job-titles-filters']/div/span").click()
    driver.find_element_by_xpath("//*[@id='jobFunctions-Sales']/label/span[1]").click()
    sales_reps = (driver.find_element_by_class_name("results-count")).text
    #sales_reps = driver.find_element_by_xpath("//*[@id='app-root']/div/div[1]/zi-pages/div/div/div/div/zi-search-core-container/zi-page-template/div/div/zi-page-content/div/div/div[2]/zi-people-results-page/div/div/div[2]/div/div/span[1]")
    print(sales_reps)
                                       
        
    
                                                                
    

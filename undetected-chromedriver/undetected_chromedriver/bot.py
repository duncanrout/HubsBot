import undetected_chromedriver.v2 as uc
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
    driver.find_element_by_xpath("//input[@placeholder ='Full Name' and @type = 'text']")

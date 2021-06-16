import undetected_chromedriver.v2 as uc
#new imports
from selenium import webdriver

## setting profile
#options.user_data_dir = "c:\\temp\\profile"
options.user_data_dir = "C:\\Users\\Duncan.Rout\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Default"

## another way to set profile is the below (which takes precedence if both variants are used
#options.add_argument('--user-data-dir=c:\\temp\\profile2')
print(5)

# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    #driver.get('https://app.hubspot.com/login/?hsCtaTracking=d82c5d82-821c-4c0d-86f5-6c34dced0e6d%7C16494015-d90f-47fc-adc3-593e2e1bdfa0')
    driver.get('https://app.hubspot.com/contacts/1734343/objects/0-2/views/5765433/list')

#email = driver.find_element_by_id("username")
#password = driver.find_element_by_id("password")

#driver.find_element_by_id("loginBtn").click()
domainLink = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/form/button[1]".click()

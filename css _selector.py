from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path="/Users/Gheethvijay/QA/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.Amazon.com/')

driver.find_element(By.CSS_SELECTOR,'#nav-link-accountList[data-nav-ref="nav_ya_signin"]').click()
sleep(4)
driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()
sleep(3)
# driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo[role="img"][aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'#ap_email')
driver.find_element(By.CSS_SELECTOR,'#ap_password')
driver.find_element(By.CSS_SELECTOR,'div[aria-atomic="true"]')
# driver.find_element(By.CSS_SELECTOR,'.a-alert-content')
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'#continue')
# driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*='condition_of_use']")
# driver.find_element(By.CSS_SELECTOR,".a-row.a-spacing-top-medium.a-size-small a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR,'[href*="gp/help/customer/display.html/ref=ap_register_notification_condition_of_use"]')
driver.find_element(By.CSS_SELECTOR,'[href*="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice"]')
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age=0&openid.']")

print('Test passed')

driver.quit()


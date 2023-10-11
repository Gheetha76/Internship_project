from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path="/Users/Gheethvijay/QA/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

driver.wait = WebDriverWait(driver, 3)


# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('chair')


# wait for 4 sec
# sleep(4)


# click search button
# driver.find_element(By.NAME, 'btnK').click()
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# verify search results
assert 'chair' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

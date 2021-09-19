from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/alerts')
driver.find_element_by_id('timerAlertButton').click()

try:
    WebDriverWait(driver, 8).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert Sudah Ditekan!")

except TimeoutException:
    print("Alert Tidak Ditemukan!")
    pass
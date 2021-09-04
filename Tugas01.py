# Tugas menampilkan Title dan Alamat secara berurutan

from selenium import webdriver

driver = webdriver.Chrome()

driver.minimize_window()

url_list = ['https://noobtest.id','https://erzaf.com/',
            'https://orangsiber.com','https://demoqa.com',
            'https://automatetheboringstuff.com']

for i in url_list :
    driver.get(i)
    print(driver.current_url,'-', driver.title)

driver.close()
    
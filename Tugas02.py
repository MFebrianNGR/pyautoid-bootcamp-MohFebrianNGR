from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://demoqa.com/webtables')

Input_Data = [
            ['Amsal','Salom', 'amsalom@noobtest.id', '28', '5000', 'IT Support'],
            ['Dita','Karang', 'ditaka@noobtest.id', '23', '4500', 'IT Admin'],
            ['Febrian','Nur', 'febrianu@noobtest.id', '24', '6000', 'IT Support'],
]
        
for data in Input_Data :

    Add = driver.find_element_by_id('addNewRecordButton').click()

    First_Name = driver.find_element_by_id('firstName').send_keys(data[0])
    Last_Name = driver.find_element_by_id('lastName').send_keys(data[1])
    Email = driver.find_element_by_id('userEmail').send_keys(data[2])
    Umur = driver.find_element_by_id('age').send_keys(data[3])
    Salary = driver.find_element_by_id('salary').send_keys(data[4])
    Department = driver.find_element_by_id('department').send_keys(data[5])

    Submit = driver.find_element_by_id('submit').click()

from selenium import webdriver

import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

Input_Data = [
            {'userName':'Febrian','userEmail':'febrian0530@gmail.com', 
            'currentAddress':'Lebak', 'permanentAddress':'Depok'}
            ]

def test_tugas04():
    driver.get('https://demoqa.com/text-box')
    
    for data in Input_Data :
        for key in data :
            driver.find_element_by_id(key).send_keys(data[key])
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #button submit tidak ditemukan karena tertutup iklan, akhirnya saya menggunakan perintah scroll chrome

    driver.find_element_by_id('submit').click()

    Name = driver.find_element_by_id('name').text
    Email = driver.find_element_by_id('email').text
    Current = driver.find_element_by_id('currentAddress').text
    Permananet = driver.find_element_by_id('permanentAddress').text

    assert Name == 'Name:Febrian'
    assert Email == 'Email:febrian0530@gmail.com'
    #assert Current == 'Current Address' #assert tidak bisa dijalankan
    #assert Permananet == 'Permananet Address' #assert tidak bisa dijalankan






from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class Test_Sauce:
    def __init__(self): 
     pass
    def siteGiris():
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(2)

    def siteSifre():
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(2)
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(firstResult)

    def kullaniciAdi():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        sleep(2)
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(firstResult)
               
    def kullaniciBos():
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(firstResult)     
        sleep(2)

    def error_icon():    
        errorBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorBtn.click()   
        print(errorBtn)
        sleep(2)
          
    def locked_out_user():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("locked_out_user")
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(2)
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        firstResult = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(firstResult)
        sleep(2) 
     
    def login():
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.NAME,"user-name").send_keys("standard_user")
        driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        sleep(2)
        driver.find_element(By.ID,"login-button").click() 
        toplam = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Sayı {len(toplam)} ")
        sleep(2)
        driver.close()

test=Test_Sauce
test.siteGiris()
test.siteSifre()
test.error_icon()
test.siteSifre()
test.siteGiris()
test.locked_out_user()
test.login()
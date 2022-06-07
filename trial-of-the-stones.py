from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path="C:\python projects\drivers\chromedriver.exe")

url ="https://techstepacademy.com/trial-of-the-stones"
browser.get(url)
time.sleep(2)

#a. Riddle of the Stone
inptfield1 = browser.find_element(By.CSS_SELECTOR, 'input[id="r1Input"]')
inptfield1.send_keys("rock")
time.sleep(2)

inptfield1btn = browser.find_element(By.XPATH, "//button[@name='r1Btn']")
inptfield1btn.click()
time.sleep(2)

firstriddleassert = browser.find_element(By.XPATH, "//h4[contains(text(),'bamboo')]").text

#b. Riddle of Secrets
inptfield2 = browser.find_element(By.CSS_SELECTOR, 'input[id="r2Input"]')
inptfield2.send_keys(firstriddleassert)
time.sleep(2)

inptfield2btn = browser.find_element(By.XPATH, "//button[@name='r2Butn']")
inptfield2btn.click()
time.sleep(2)

#c. The Two Merchants
richest_merchant = browser.find_element(By.XPATH,"//p[text()='3000']/../span").text

inptfield3 = browser.find_element(By.CSS_SELECTOR, 'input[id="r3Input"]')
inptfield3.send_keys(richest_merchant)
time.sleep(2)

inptfield3btn = browser.find_element(By.XPATH, "//button[@name='r3Butn']")
inptfield3btn.click()
time.sleep(2)


inptfield4 = browser.find_element(By.XPATH, "//button[@name='checkButn']")
inptfield4.click()
time.sleep(2)

#assertion
success = browser.find_element(By.XPATH, "//h4[contains(text(),'Trial Complete')]").text
real_success = "Trial Complete"
if success == real_success:
    print("Great Success!")
else:
    print("Try again.")
time.sleep(2)
browser.quit()
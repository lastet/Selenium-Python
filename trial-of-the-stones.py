from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


browser = webdriver.Chrome(executable_path="C:\python projects\drivers\chromedriver.exe")

url ="https://techstepacademy.com/trial-of-the-stones"
browser.get(url)
WebDriverWait(browser, 10).until(presence_of_element_located((By.CSS_SELECTOR, 'input[id="r1Input"]')))

#a. Riddle of the Stone
inptfield1 = browser.find_element(By.CSS_SELECTOR, 'input[id="r1Input"]')
inptfield1.send_keys("rock")
print("Answer 1 field is found")

inptfield1btn = browser.find_element(By.XPATH, "//button[@name='r1Btn']")
inptfield1btn.click()
print("Answer 1 is in")

firstriddleassert = browser.find_element(By.XPATH, "//h4[contains(text(),'bamboo')]").text

#b. Riddle of Secrets
inptfield2 = browser.find_element(By.CSS_SELECTOR, 'input[id="r2Input"]')
inptfield2.send_keys(firstriddleassert)
print("Answer 2 field is found")

inptfield2btn = browser.find_element(By.XPATH, "//button[@name='r2Butn']")
inptfield2btn.click()
print("Answer 2 is in")

#c. The Two Merchants
richest_merchant = browser.find_element(By.XPATH,"//p[text()='3000']/../span").text

inptfield3 = browser.find_element(By.CSS_SELECTOR, 'input[id="r3Input"]')
inptfield3.send_keys(richest_merchant)
print("Richest Merchant name is in")

inptfield3btn = browser.find_element(By.XPATH, "//button[@name='r3Butn']")
inptfield3btn.click()
print("Answer 3 is in")


#Complete button
inptfield4 = browser.find_element(By.XPATH, "//button[@name='checkButn']")
inptfield4.click()
print("Complete button clicked")

#assertion
success = browser.find_element(By.XPATH, "//h4[contains(text(),'Trial Complete')]").text
real_success = "Trial Complete"
if success == real_success:
    print("Great Success!")
else:
    print("Try again.")

browser.quit()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

url = "https://www.booking.com"
browser.get(url)

search_string = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/div[1]/div[1]/div[1]/label/input")
search_string.send_keys("par")
time.sleep(2)

search_pick = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]")
search_pick.click()

pick_date1 = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[6]/span/span")
pick_date1.click()
pick_date2 = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[4]/span/span")
pick_date2.click()
time.sleep(1)

look_prices = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/div[4]/div[2]/button")
look_prices.click()
time.sleep(3)

optnbtn = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/div/div/div[2]/ul/li[10]/a")
optnbtn.click()
time.sleep(1)

distancebtn = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/div/div/div[2]/ul/li[10]/ul/li[5]/a")
distancebtn.click()
time.sleep(7)

opnmap = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div/div/div/span")
opnmap.click()
time.sleep(7)

filter_map = browser.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div[1]/div/button")
filter_map.click()
time.sleep(1)

five_pick = browser.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div[1]/div/div/div/ul/li[4]/button")
five_pick.click()
time.sleep(5)

hotel01 = browser.find_element(By.XPATH, "/html/body/div[9]/div[3]/div[2]/div[2]/div/a[3]/div[3]/div[1]/span")
hotel01.click()
time.sleep(7)

browser.maximize_window()
time.sleep(4)

browser.quit()




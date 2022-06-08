from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\python projects\drivers\chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def temp_only(text):
    output = float(text.split(": ")[1])
    return output

def main():
  driver = get_driver()
  #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  #//*[@id="displaytimer"]
  #element = driver.find_element(by="id", value="displaytimer")
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return temp_only(element.text)

print(main())
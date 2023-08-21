import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(12)
                           

browser.maximize_window()
browser.get("https://chercher.tech/practice/frames")


iframe1 = browser.find_element(By.ID, "frame1")
browser.switch_to.frame(iframe1)

browser.find_element(By.XPATH, "/html/body/input").send_keys("iframe1")
time.sleep(2)
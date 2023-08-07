import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.google.com.br/")
time.sleep(5)

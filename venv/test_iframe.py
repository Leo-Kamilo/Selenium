import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)
                           

browser.maximize_window()
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
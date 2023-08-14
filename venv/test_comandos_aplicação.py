import time
from selenium import webdriver

browser = webdriver.Chrome() 

browser.get("https://www.saucedemo.com/")

print('O titulo da pagina é:', browser.title)

print('A UL da pagina é:', browser.current_url)

print('O codigo-fonte da pagina é', browser.page_source)
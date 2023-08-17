# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome() 

# browser.maximize_window()
# browser.get("https://www.saucedemo.com/")

# num_esperado = 2
# num_obtido = 2
# assert num_esperado == num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}."

text_esperado = "Selenium"
text_obtido = "Selenium Webdriver"
assert text_esperado not in text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."
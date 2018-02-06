import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import selenium
from selenium import webdriver
import openpyxl

#  Acessa os dados de login fora do script, salvo numa planilha existente, para proteger as informações de credenciais
dados = openpyxl.load_workbook('C:\\gomnet.xlsx')
login = dados['Plan1']
url = 'http://gomnet.ampla.com/'
consulta = 'http://gomnet.ampla.com/ConsultaObra.aspx'
username = login['A1'].value
password = login['A2'].value

# --------------- Headless Mode -------------------------
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : os.getcwd(),
#          "download.prompt_for_download": False}
# chromeOptions.add_experimental_option("prefs",prefs)
# chromeOptions.add_argument('--headless')
# chromeOptions.add_argument('--window-size= 1600x900')
# driver = webdriver.Chrome(chrome_options=chromeOptions)
# -------------------------------------------------------

driver = webdriver.Chrome()

if __name__ == '__main__':
    driver.get(url)
    # Faz login no sistema
    uname = driver.find_element_by_name('txtBoxLogin')
    uname.send_keys(username)
    passw = driver.find_element_by_name('txtBoxSenha')
    passw.send_keys(password)
    submit_button = driver.find_element_by_id('ImageButton_Login').click()
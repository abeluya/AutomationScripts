from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def exist_element(driver, chat_Id):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, chat_Id)))
        #driver.find_element_by_id(chat_Id)
        return True
    except:
        return False

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)

linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)

countries = ["de", "es", "fr","pt","ja","zh","ko"]
className = 'intercom-fvs20o e2ujk8f2'
chatId = "intercom-container"

for line in linelList:
    if line is not '':
        driver.get(line)
        print(line + " : " +  str(exist_element(driver, chatId)))
        for country in countries:
            url = line.replace('com/','com/'+ country +'/')
            driver.get(url)
            print(url + " : " + str(exist_element(driver, chatId)))

driver.quit()
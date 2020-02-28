from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def exist_element(driver, selector_name, class_name):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_name)))
        driver.find_element_by_class_name(class_name)

        return True
    except:
        return False

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)

countries = ["de", "es", "fr","pt","ja","zh","ko"]
className = 'fort-sw-security-prod-servu-mft'
#className = "fort-sw-security-prod-kiwi-syslog-log-management"
cssSelector = "body > div.container-fluid > div:nth-child(1) > nav"

for line in linelList:
    if line is not '':
        driver.get(line)
        print(line + " : " +  str(exist_element(driver, cssSelector, className)))

driver.quit()
from tkinter import Tk
from selenium import webdriver


author = "https://author.azure.solarwinds.com/sitemap"
live = "https://www.solarwinds.com/sitemap"

driver = webdriver.Chrome()
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)

print("Origin || Destiny" )
for line in linelList:
    if line is not '':
        driver.get(line)
        destiny = driver.current_url
        print(line + "    " + destiny)
    else:
        print("Blank")
driver.quit()
from tkinter import Tk
from selenium import webdriver


author = "https://author.azure.solarwinds.com/sitemap.xml"
live = "https://www.solarwinds.com/sitemap.xml"

driver = webdriver.Chrome()
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
cont = 0
for line in linelList:
    print(line)
    if line is not '':
        cont += 1
print("Total URLS: " + cont.__str__())
driver.get(live)
good = 0
bad = 0

for line in linelList:
    if line is not '':
        #print("Buscando " + array[0])
        try:
            element = driver.find_element_by_xpath("//*[text()=\"" + line+"\"]")
            link = element.get_attribute("href")
            #print(link)
            if line != link:
                print(line + ": Not Found")
                bad += 1
            else:
                print(line + ": OK")
                good += 1
            #print(array[0] + "= " + element.text)
        except:
            print(line + ": Not Found")
print("Good URLS: " + good.__str__())
print("Bad URLS: " + bad.__str__())

driver.quit()
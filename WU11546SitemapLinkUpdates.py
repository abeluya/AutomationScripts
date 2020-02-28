from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



author = "https://author.azure.solarwinds.com/sitemap"
live = "https://www.solarwinds.com/sitemap"

driver = webdriver.Chrome()
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)
driver.get(author)
driver.implicitly_wait(10) # seconds

for line in linelList:
    if line is not '':
        array = line.split('\t')
        #print("Buscando " + array[0])
        try:
            element = driver.find_element_by_xpath("//*[text()=\"" + array[0]+"\"]")
            link = element.get_attribute("href")
            #print(link)
            if array[1] != link:
                print(array[0] + ": Check URL")
            #else:
                #print(array[0] + " Check URL")
            #print(array[0] + "= " + element.text)
        except:
            print(array[0] + ": Not Found")
driver.quit()
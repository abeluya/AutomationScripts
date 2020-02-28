from tkinter import Tk
from selenium import webdriver



driver = webdriver.Chrome()
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)


for line in linelList:
    if line is not '':
        array = line.split('\t')
        driver.get(array[0])
        #print("Buscando " + array[0])
        try:
            #assert driver.page_source.find(array[1])
            # element = driver.find_element_by_xpath("//*[text()=\"" + array[1]+"\"]")
            texto = driver.page_source
            #print(link)
            legacy = '"legacyPageName": "' + array[1] + '"'
            if legacy in texto:
                print(array[0] + ": OK")
            else:
                print(array[0] + " Check Legacy PageName")
            #print(array[0] + "= " + element.text)
        except:
            print(array[0] + ": Not Found")

driver.quit()
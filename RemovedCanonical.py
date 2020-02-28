from tkinter import Tk
from selenium import webdriver

def exist_element(driver, classname):
    try:
        e = driver.find_element_by_xpath(classname)

        return e
    except:
        return False


author = "https://author.azure.solarwinds.com/sitemap"
live = "https://www.solarwinds.com/sitemap"
countries = ["de", "es", "fr","pt","ja","zh","ko"]

driver = webdriver.Chrome()
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)

for line in linelList:
    if line is not '':
        x = line.split('\t')
        driver.get(x[0])
        #print("Page: " + x[0])
        #print("Canonical: " + x[1])
        #print("Buscando " + array[0])
        try:
            ## element = driver.find_element_by_xpath("//*[text()=\"" + array[0]+"\"]")
            element = driver.find_element_by_xpath("/html/head/link[3]")
            link = str(element.get_attribute("href"))
            #print(link)
            if str(x[1]) == link:
                print(x[1] + ": OK")
            else:
                print(x[1] + ": Check Canonical")
            #print(array[0] + "= " + element.text)
            #for country in countries:
             #   url = line.replace('com/','com/'+ country +'/')
              #  driver.get(url)
               # element = driver.find_element_by_xpath("/html/head/link[3]")
                #link = element.get_attribute("href")
                #if url != link:
                 #   print(url + ": Check Canonical")
                #else:
                 #   print(url + ": OK")
        except:
            print(line + ": Not Found")
driver.quit()
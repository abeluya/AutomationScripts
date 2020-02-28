from tkinter import Tk
from selenium.webdriver.chrome.options import Options

from selenium import webdriver


options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)
linelList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(linelList))
print(linelList)
for line in linelList:
    print(line)

countries = ["de", "es", "fr","pt","ja","zh","ko"]
text = "View All Access Rights Manager Use Cases"
className = "topic-backlink-container"


for line in linelList:
    if line is not '':
        driver.get(line)
        try:
            #element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[1]/a')
            element = driver.find_element_by_class_name('topic-backlink-container')
            print(line + " Remove")
        except:
            print(line + ": Ok")

        for country in countries:
            url = line.replace('com/','com/'+ country +'/')
            driver.get(url)
            try:
                #element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[1]/a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ')
                element = driver.find_element_by_class_name('topic-backlink-container')
                print(url + " Remove")
            except:
                print(url + ": Ok")


driver.quit()
from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\Rishabh Malik\Downloads\chromedriver_win32.zip')

driver.get('http://python.org')

#this will contain the page source
html_doc=driver.page_source

print(html_doc)
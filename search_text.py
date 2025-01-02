from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Download ChromeDrive
# https://sites.google.com/chromium.org/driver/

Service = Service(executable_path="chromedriver.exe")

# 创建一个Chrome实例，并将service对象传入。
driver = webdriver.Chrome(service=Service)


# get()是webdriver对象的一个方法，用于让浏览器打开网页。
driver.get("https://linux.mainframe.blog/")

search = driver.find_element(By.CLASS_NAME, "search-field")
search.send_keys("linuxone")
search.send_keys(Keys.ENTER)

# main 是一个大的div，articles都包含在这个div内部

try:
    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    
    # 每个文章都是包在这样一个标签中的 <article>，这个叫tag
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-title")
        print(header.text)




finally:
    driver.quit()



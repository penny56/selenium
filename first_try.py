from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# Download ChromeDrive
# https://sites.google.com/chromium.org/driver/



# 创建一个webDriver实例，来控制browser
Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# 旧的创建方法（过时）
# driver = webdriver.Chrome('./chromedriver')

# load a website，用于让浏览器打开网页。
driver.get("https://google.com")

# 等待（最多5秒），直到 "gLFyf" located完
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# 这里不止class_name，还有其它可以find，比如ID
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("content" + Keys.ENTER)

# 在搜索结果页面，我们要找到content页面的链接，并且点开它。
# 这里只会找1st，如果要把全部包括 content 的link，则需要用 find_elements()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "content"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "content") 
link.click()


time.sleep(10)
driver.quit()
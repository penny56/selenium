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
Service = Service(executable_path="C:\\Users\\penny\\git\\selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=Service)

# 旧的创建方法（过时）
# driver = webdriver.Chrome('./chromedriver')

# load a website，用于让浏览器打开网页。
driver.get("https://www.google.com/?hl=en-US")

# Wait (max 10s) for the popup to appear
popup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Accept all']"))
)

# Click the "Accept" button
popup.click()

# 搜索 content，这里不止class_name，还有其它可以find，比如ID
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("content" + Keys.ENTER)

# 在搜索结果页面，我们要找到content页面的链接，并且点开它。
# 这里只会找1st，如果要把全部包括 content 的link，则需要用 find_elements()
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "content"))
# )

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "content") 
# link.click()

wait = WebDriverWait(driver, 10)  # Adjust timeout as needed
wait.until(EC.invisibility_of_element_located((By.ID, "sfcnt"))) 

link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@jsname='BKxS1e']"))) 
link.click()

time.sleep(10)
driver.quit()














from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/?hl=en-US")

# Wait for the popup to appear
popup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Accept all']"))
)

# Click the "Accept" button
popup.click()

time.sleep(5)

# Proceed with your tests
'''
Test case 5: TimeoutException
1. Open page
2. Click Add button
3. Wait for 3 seconds for the second input field to be displayed
Verify second input field is displayed
The second row shows up after about 5 seconds, so a 3-second timeout is not enough. That’s why we will get TimeoutException while executing steps in the above test case.

重点：等待超时，触发 TimeoutException，重点在于：
- 使用 WebDriverWait 配合较短的超时时间（如题目要求：等待 3 秒）
- 由于页面元素大约 5 秒才出现，因此等待会超时，正确地捕获 TimeoutException。。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")

try:
    # 点击 add 按钮
    driver.find_element(By.ID, "add_btn").click()

    # 设置3秒等待时间，等待第2个输入框
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input"))
    )

    print("The second input field appeared within 3 seconds (unexpected).")

except TimeoutException:
    print("The TimeoutException was triggered as expected.")

finally:
    driver.quit()
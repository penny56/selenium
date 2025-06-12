'''
Test case 4: StaleElementReferenceException
1. Open page
2. Find the instructions text element
3. Push add button
4. Verify instruction text element is no longer displayed
The instructions element is removed from the page when the second row is added. That’s why we can no longer interact with it. Otherwise, we will see StaleElementReferenceException.

重点：元素在页面 DOM 中被删除或更新，导致你手上保存的 WebElement 变成了“失效元素”，这时候如果你还试图操作或检查它，就会抛出 StaleElementReferenceException。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 陈旧元素引发异常
from selenium.common.exceptions import StaleElementReferenceException

import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")

try:
    instructions = driver.find_element(By.ID, "instructions")

    # 点击 add 按钮
    driver.find_element(By.ID, "add_btn").click()

    # 确保DOM更新
    time.sleep(2)

    # 尝试访问已删除元素
    print(instructions.text)

except StaleElementReferenceException:
    print("The StaleElementReferenceException was triggered as expected.")

finally:
    time.sleep(2)
    driver.quit()
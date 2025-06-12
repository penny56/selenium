'''
Test case 1: NoSuchElementException
1. Open page
2. Click Add button
3. Verify Row 2 input field is displayed
Row 2 doesn’t appear immediately. This test will fail with org.openqa.selenium.NoSuchElementException without proper wait

关键：需要显式等待 Row 2 的输入框出现，否则会抛出 NoSuchElementException。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")

try:
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()

    # 没有等待，直接查找
    row2_input = driver.find_element(By.XPATH, "//div[@id='row2']//input[@type='text']")

    assert row2_input.is_displayed()
    print("Row 2 input field is displayed.")

except NoSuchElementException:
    print("NoSuchElementException: Row 2 input field was not found (no wait applied).")


finally:
    time.sleep(2)
    driver.quit()
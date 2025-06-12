'''
Test case 2: ElementNotInteractableException
1. Open page
2. Click Add button
3. Wait for the second row to load
4. Type text into the second input field
5. Push Save button using locator By.name(“Save”)
6. Verify text saved
This page contains two elements with attribute name=”Save”.
The first one is invisible. So when we are trying to click on the invisible element, we get ElementNotInteractableException.

The same action used to throw ElementNotVisibleException, but now it throws a different exception (not sure if it’s a bug in Selenium or a feature)

重点：页面上有两个 name="Save" 的按钮，第一个是不可见的，点击会触发 ElementNotInteractableException。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-exceptions/")

try:
    add_button = driver.find_element(By.ID, "add_btn")
    add_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='row2']//input[@type='text']"))
    )

    row2_input = driver.find_element(By.XPATH, "//div[@id='row2']//input[@type='text']")
    row2_input.send_keys("Pasta")

    # 注意，这里是故意找错 Save button
    save_buttons = driver.find_elements(By.NAME, "Save")

    try:
        # 注意，这里取的[0]也是取的不可click()的那个
        save_buttons[0].click()
    except ElementNotInteractableException:
        print("The ElementNotInteractableException was triggered as expected.")

finally:
    time.sleep(2)
    driver.quit()
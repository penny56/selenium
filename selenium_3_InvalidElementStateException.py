'''
Test case 3: InvalidElementStateException
1. Open page
2. Clear input field
3. Type text into the input field
4. Verify text changed
The input field is disabled. Trying to clear the disabled field will throw InvalidElementStateException. We need to enable editing of the input field first by clicking the Edit button.

If we try to type text into the disabled input field, we will get ElementNotInteractableException, as in Test case 2.

重点：输入框处于禁用状态（disabled）（不是readonly，readonly是可被选中，而disabled是完全不可交互）时：
- 如果执行 clear()	，则会抛出：InvalidElementStateException
- 如果执行 send_keys()	，则会抛出：ElementNotInteractableException （同case 2)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import InvalidElementStateException, ElementNotInteractableException

import time

def test_invalid_element_state_exception():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        input_field = driver.find_element(By.XPATH, "//input[@value='Pizza']")
    
        try:
            input_field.clear()
            print("Test failed: InvalidElementStateException was not raised as expected.")
        
        except InvalidElementStateException:
            # 如果是要 clear() 的时候，会出这个 exception
            # 如果是
            print("Test passed: InvalidElementStateException was triggered as expected.")
        
        # 点击 Edit 启用输入框
        driver.find_element(By.ID, "edit_btn").click()

        # 输入测试文本
        input_field.clear()
        input_field.send_keys("Pasta")

        # 获取当前输入框内容并打印
        current_value = input_field.get_attribute("value")

        if current_value == "Pasta":
            print("Input field text updated successfully.")
        else:
            print("Test failed: Input field text was not updated.")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_invalid_element_state_exception()
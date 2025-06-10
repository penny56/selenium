from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import time

class LoginPage:
    username = 'student'
    neg_username = 'incorrectUser'
    password = 'Password123'

    def __init__(self, driver):
        self.driver = driver

        # tuple 输入法，在 EC.visibility_of_element_located() 中使用
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'submit')

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)
    
    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

def login_test():
    # 初始化 webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1) # 防止极短延迟报错

    try:
        print("示例登录页面...")
        driver.get('https://practicetestautomation.com/practice-test-login/')
        login_page = LoginPage(driver)

        print("开始登录流程...")
        login_page.login(login_page.neg_username, login_page.password)


        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Your username is invalid!')
        )
        print('页面包含预期文本！')

        
    except TimeoutException:
        print('登录失败：页面加载超时或元素未找到')

    except NoSuchElementException:
        print('登录失败：元素不存在')

    finally:
        time.sleep(1)
        driver.quit()

if __name__ == '__main__':
    login_test()
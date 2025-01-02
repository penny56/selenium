from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Download ChromeDrive
# https://sites.google.com/chromium.org/driver/

Service = Service(executable_path="chromedriver.exe")

# 创建一个Chrome实例，并将service对象传入。
driver = webdriver.Chrome(service=Service)


# get()是webdriver对象的一个方法，用于让浏览器打开网页。
driver.get("https://orteil.dashnet.org/cookieclicker/")

# 首先它会要求你选择 language
# XPATH 可以让你 search 一些属性，问GPT："页面中间有一个语言选择器，我想通过selenium自动点选English这一项，但是不知道怎么设置XPATH"，再把html中选择language这一段粘贴上去。

# Wait until the "English" language button is clickable
english_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )

english_button.click()

# 拿到按钮的ID
# 最好的选择是search by ID，其次是 by class，再次是 by name
cookie_id = "bigCookie"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

# 计算现在已有多少cookies
# <div id="cookies"
cookies_id = "cookies"
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

product_prefix = "product"
product_price_prefix = "productPrice"

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", "")) # 处理 1,000 这种
    
    # 有4种可以加成的属性：product0~product4
    # 如果我们现有的 cookies_count > 要求的cookies_count，就click()
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break





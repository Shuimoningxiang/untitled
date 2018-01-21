from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("http://172.31.4.74")
driver.find_element_by_link_text("注册").click()
window=driver.current_window_handle
windows=driver.window_handles
for handle in windows:
    if handle!=window:
        driver.close()
# driver.implicitly_wait(5)
# driver.find_element_by_sname("").send_keys("ssuo")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_name("userpassword2").send_keys("123456")
# driver.find_element_by_name("mobile_phone").send_keys("13522222222")
# driver.find_element_by_name("email").send_keys("456798@qq.com")
# driver.find_element_by_class_name("reg_btn").submit()


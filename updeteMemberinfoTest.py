import unittest
import time
from selenium import webdriver

from myTestCase import MyTestCase


class UpdateMemberInfoText(MyTestCase):

    def test_member_updating(self):
        driver=self.driver
        print("这是一个测试用例方法,这个方法用于修改会员信息的测试")
        driver.find_element_by_link_text("账号设置").click()
        driver.find_element_by_link_text("个人资料").click()
        driver.find_element_by_name("true_name").clear()
        driver.find_element_by_name("true_name").send_keys("完善个更息")
        driver.find_element_by_xpath("//input[@value='1']").click()
        driver.find_element_by_class_name("btn4").submit()
        driver.execute_script("document.getElementById(\"date\").removeAttribute(\"readonly\")")
        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("1999-9-10")
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys("5459684321")
        driver.find_element_by_class_name("btn4").submit()
        time.sleep(5)
        driver.switch_to.alert.accept()
    def test_denglu(self):
        driver=self.driver
        print("这是登陆的测试用例")
        driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("username11")
        driver.find_element_by_id("password").send_keys("username")
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/ul/li[5]/input").click()
if __name__=='__main__':
    unittest.main
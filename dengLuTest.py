

from DengLuPage import LoginPage
from myTestCase import MyTestCase


class DengLuTest(MyTestCase):
    def test_login(self):
        loginpage=LoginPage(self.driver)
        loginpage.login("username11", "username")

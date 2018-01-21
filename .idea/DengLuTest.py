class DengLuTest(MyTestCase):
    def test_login(self):
        loginPage=LoginPage(self.driver)
        loginPage.login("username11","username")

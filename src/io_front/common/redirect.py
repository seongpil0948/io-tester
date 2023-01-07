import unittest
from config import ENTRY_URL
from urllib.parse import urlparse
from os.path import join as pjoin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ...base import IoTestBase, TestWithSelenium


class FrontRedirectTest(TestWithSelenium, IoTestBase):
    def setUp(self, name_it="hi"):
        # name = self.__class__.__name__
        self.setupSelenium()
        self.url = ENTRY_URL

    # def testRedirectLogin(self):
    #     self.driver.get(self.url)
    #     u = urlparse(self.driver.current_url)
    #     print("entry url: ", u)
    #     self.assertEqual(u.path, "/login")

    # def testRedirectSignup(self):

    def testFailLogin(self):
        self.driver.get(pjoin(self.url, "login"))
        self.driver.implicitly_wait(20)
        self.getBySel(
            "input-email").find_element(By.TAG_NAME, "input").send_keys("bla bla")
        self.getBySel("input-pw").find_element(By.TAG_NAME,
                                               "input").send_keys("bla bla")
        self.driver.find_element(By.ID, "login-page-container").click()
        allTxt = self.driver.find_element(By.ID, "login-page-container").text
        self.assertIn("유효한 이메일 주소를 입력 해주세요.", allTxt)
        self.assertIn("영문, 숫자", allTxt)

    # def testIsupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def testSplit(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         # will be TypeError: must be str or None, not int
    #         s.split(2)
        # self.assertTrue('FOO'.isupper())
        # self.assertFalse('Foo'.isupper())

    def tearDown(self):
        self.tearDownSelenium()


if __name__ == '__main__':
    runner = unittest.TextTestRunner(
        descriptions="[Suite] FrontRedirectTest ", verbosity=2)
    suite = unittest.TestSuite()
    suite.addTests(FrontRedirectTest.listTest())
    result = runner.run(suite)

    # unittest.main(verbosity=2)

from abc import ABCMeta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.util.driver import get_driver


class TestWithSelenium(metaclass=ABCMeta):
    @classmethod
    def setupSelenium(cls):
        cls.driver = get_driver()

    @classmethod
    def tearDownSelenium(cls):
        cls.driver.close()
        cls.driver.quit()

    def getBySel(self, selector):
        # return WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-test=${selector}]")))
        return self.driver.find_element(By.CSS_SELECTOR, f"[data-test={selector}]")

    def listBySel(self, selector):
        # return WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-test=${selector}]")))
        return self.driver.find_elements(By.CSS_SELECTOR, f"[data-test={selector}]")

    def listBySelLike(self, selector):
        # return WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-test=${selector}]")))
        return self.driver.find_elements(By.CSS_SELECTOR, f"[data-test*={selector}]")

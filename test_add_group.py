# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()  # Firefox запускается, если установлен geckodriver
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        # password send
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        # click login
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        # return to groups page
        wd.find_element(By.LINK_TEXT, "groups").click()
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def init_group_creation(self, wd):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("dfidifk")
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("fjjsdf")
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("dsfjjjsdf")
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def open_groups_page(self, wd):
        # open group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, wd):
        # login
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

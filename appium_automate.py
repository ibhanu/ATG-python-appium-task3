import os
import unittest
from appium import webdriver
from time import sleep
 
class ATG(unittest.TestCase):
    "Class to run tests against the ATG app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {
         "platformName": "android",
  "appActivity": "com.atg.world.activity.SplashActivity",
  "appWaitDuration": 50,
  "uiautomator2ServerLaunchTimeout": 50000,
  "uiautomator2ServerInstallTimeout": 50000,
  "appPackage": "com.ATG.World",
  "deviceName": "Mi A3",
  "driver": "http://localhost:4723/wd/hub" }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_atg(self):
        "Test the ATG app launches correctly and Automade the login"
        getstarted = self.driver.find_element_by_id("com.ATG.World:id/getStartedTv")
        getstarted.click()
        sleep(0.5)
        log = self.driver.find_element_by_id("com.ATG.World:id/login_email")
        log.click()
        sleep(0.5)
        email = self.driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = self.driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = self.driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()

        sleep(10)
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ATG)
    unittest.TextTestRunner(verbosity=2).run(suite)


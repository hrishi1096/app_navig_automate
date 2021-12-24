from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from threading import Thread
import pytest

IMPLICIT_WAIT_TIME = 10
EXPLICIT_WAIT_TIME = 30
USERNAME = os.environ['BROWSERSTACK_USERNAME']
ACCESSKEY = os.environ['BROWSERSTACK_ACCESS_KEY']
BUILD_NAME = os.environ['BROWSERSTACK_BUILD_NAME']
APPID = os.environ["BROWSERSTACK_APP_ID"]
DELAY = 3


capabilities = [
    {
    "app" : APPID,
    "device" : "Samsung Galaxy S21 Ultra",
    "os_version" : "11.0",
    "real_mobile" : "true",
    "browserstack.networkLogs": "true",
    "browserstack.debug": "true",
    "project" : "App Automate assignment",
    "build" : BUILD_NAME,
    "name" : "Galaxy S21 ultra",
    "browserstack.appium_version" : "1.20.2",
    "browserstack.networkLogs" : "true",
    # "browserstack.timezone" : "India",
    "browserstack.networkProfile" : "3.5g-hspa-plus-lossy",
    "deviceOrientation" : "landscape",
    # "browserstack.geoLocation": "IN",
    "browserstack.console" : "verbose"
    },
    {
    "app" : APPID,
    "device" : "Google Pixel 5",
    "os_version" : "11.0",
    "real_mobile" : "true",
    "browserstack.networkLogs": "true",
    "browserstack.debug": "true",
    "project" : "App Automate assignment",
    "build" : BUILD_NAME,
    "name" : "Pixel 5",
    "browserstack.appium_version" : "1.20.2",
    "browserstack.networkLogs" : "true",
    # "browserstack.timezone" : "India",
    "browserstack.networkProfile" : "3.5g-hspa-plus-lossy",
    "deviceOrientation" : "landscape",
    # "browserstack.geoLocation": "IN",
    "browserstack.console" : "verbose"
    },
    {
    "app" : APPID,
    "device" : "OnePlus 9",
    "os_version" : "11.0",
    "real_mobile" : "true",
    "browserstack.networkLogs": "true",
    "browserstack.debug": "true",
    "project" : "App Automate assignment",
    "build" : BUILD_NAME,
    "name" : "Oneplus 9",
    "browserstack.appium_version" : "1.20.2",
    "browserstack.networkLogs" : "true",
    # "browserstack.timezone" : "India",
    "browserstack.networkProfile" : "3.5g-hspa-plus-lossy",
    "deviceOrientation" : "landscape",
    # "browserstack.geoLocation": "IN",
    "browserstack.console" : "verbose"
    },
    {
    "app" : APPID,
    "device" : "Samsung Galaxy Tab S7",
    "os_version" : "10.0",
    "real_mobile" : "true",
    "browserstack.networkLogs": "true",
    "browserstack.debug": "true",
    "project" : "App Automate assignment",
    "build" : BUILD_NAME,
    "name" : "Galaxy tab S7",
    "browserstack.appium_version" : "1.20.2",
    "browserstack.networkLogs" : "true",
    # "browserstack.timezone" : "India",
    "browserstack.networkProfile" : "3.5g-hspa-plus-lossy",
    "deviceOrientation" : "landscape",
    # "browserstack.geoLocation": "IN",
    "browserstack.console" : "verbose"
    },
    {
    "app" : APPID,
    "device" : "Samsung Galaxy Tab S7",
    "os_version" : "10.0",
    "real_mobile" : "true",
    "browserstack.networkLogs": "true",
    "browserstack.debug": "true",
    "project" : "App Automate assignment",
    "build" : BUILD_NAME,
    "name" : "Galaxy Tab S7",
    "browserstack.appium_version" : "1.20.2",
    "browserstack.networkLogs" : "true",
    # "browserstack.timezone" : "India",
    "browserstack.networkProfile" : "3.5g-hspa-plus-lossy",
    "deviceOrientation" : "landscape",
    # "browserstack.geoLocation": "IN",
    "browserstack.console" : "verbose"
    }
]




class TestClass():
    def setup_class(self):
        # Code bindings for starting Browserstack Local with `--force-local` flag
        # uncomment if local needs to be used
        # self.bs_local = Local()
        # self.bs_local_args = {"key": ACCESSKEY, "forcelocal": "true"}
        # self.bs_local.start(**self.bs_local_args)
        pass

    def teardown_class(self):
        # uncomment if local needs to be used
        # self.bs_local.stop()
        pass

    def setup_method(self):
        self.test_successful = False

    def teardown_method(self):
        if self.test_successful:
            self.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"passed", "reason": "Navigation successful!"}}')
        else:
            self.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"failed", "reason": "Navigation unsuccessful"}}')
        self.driver.quit()

    # Some helper functions
    def get_element_with_id(self, elem_id):
        return WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.element_to_be_clickable((MobileBy.ID, elem_id)))

    def get_element_with_xpath(self, xpath):
        return WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    # Navigation test
    @pytest.mark.parametrize('desired_cap', capabilities)
    def test_app_navigation(self, desired_cap):
        # Setup the driver
        self.driver = webdriver.Remote(
            command_executor='https://' + USERNAME + ':' + ACCESSKEY + '@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)

        # Permission pop up comes up twice, deny both the times as we are not actually
        # going to inject any image
        self.get_element_with_id("com.android.permissioncontroller:id/permission_deny_button").click()
        self.get_element_with_id("com.android.permissioncontroller:id/permission_deny_button").click()

        # Click on the 'PDF Reader' tab
        self.get_element_with_xpath("//android.widget.TextView[@text='PDF Reader']").click()

        # Click on 'View Files'
        self.get_element_with_id("com.image.to.pdf.converter:id/passwordProtectedPDF").click()

        # Click on the drawer icon
        self.get_element_with_id("com.image.to.pdf.converter:id/drawerIcon").click()

        # Click on 'Home'
        self.get_element_with_xpath("//android.widget.CheckedTextView[@text='Home']").click()

        # Get the title
        title = self.get_element_with_id("com.image.to.pdf.converter:id/customTitle")
        assert(title.text == "PDF CONVERTER")

        self.test_successful = True




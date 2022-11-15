from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class Test(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def teardown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(15)
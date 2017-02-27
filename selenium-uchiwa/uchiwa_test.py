from browser import Browser
import unittest
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep


class UchiwaSelenium(unittest.TestCase):

    EVENTS = '#/events'
    CLIENTS = '#/clients'
    CHECKS = '#/checks'
    SILENCED = '#/silenced'
    STASHES = '#/stashes'
    AGGREGATES = '#/aggregates'
    DATACENTERS = '#/datacenters'

    def setUp(self):
        browser.start()

    def _url_load(self, url):
        browser.load_page_site(url)
        return browser.driver

    def _url_test(self, url, text):
        driver = self._url_load(url)
        assert text in driver.title

    def test_uchiwa_login(self):
        self._url_load(UchiwaSelenium.EVENTS)
        browser.wait_for_obj(EC.title_is('Events | Uchiwa'))

    def test_uchiwa_events(self):
        self._url_load(UchiwaSelenium.EVENTS)
        browser.wait_for_obj(EC.title_is('Events | Uchiwa'))

    def test_uchiwa_clients(self):
        self._url_load(UchiwaSelenium.CLIENTS)
        browser.wait_for_obj(EC.title_is('Clients | Uchiwa'))

    def test_uchiwa_checks(self):
        self._url_load(UchiwaSelenium.CHECKS)
        browser.wait_for_obj(EC.title_is('Checks | Uchiwa'))

    def test_uchiwa_silenced(self):
        self._url_load(UchiwaSelenium.SILENCED)
        browser.wait_for_obj(EC.title_is('Silenced | Uchiwa'))

    def test_uchiwa_stashes(self):
        self._url_load(UchiwaSelenium.STASHES)
        browser.wait_for_obj(EC.title_is('Stashes | Uchiwa'))

    def test_uchiwa_aggregates(self):
        self._url_load(UchiwaSelenium.AGGREGATES)
        browser.wait_for_obj(EC.title_is('Aggregates | Uchiwa'))

    def test_uchiwa_datacenters(self):
        self._url_load(UchiwaSelenium.DATACENTERS)
        browser.wait_for_obj(EC.title_is('Datacenters | Uchiwa'))
    '''
    def _uchiwa_search(self, text, items):
        self._url_load(UchiwaSelenium.CLIENTS)
        browser.wait_for_obj(EC.title_is('Clients | Uchiwa'))
        sleep(1)
        inputtext = browser.wait_for_obj(EC.visibility_of_element_located(
            (By.XPATH, '//input[@ng-model=\'filters.q\']')
        ))
        inputtext.send_keys(text)
        search = browser.wait_for_obj(EC.presence_of_element_located(
            (By.CLASS_NAME, 'search-results')
        ))
        assert items in search.text

    def test_uchiwa_1_localhost(self):
        self._uchiwa_search('localhost', '1 Items')
    '''
    def tearDown(self):
        browser.end()


if __name__ == "__main__":
    browser = Browser(screenshot_on_error=True)
    browser.parse_arguments()
    browser.set_url('uchiwa')
    unittest.main()

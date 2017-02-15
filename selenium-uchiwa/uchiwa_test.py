import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class UchiwaSelenium(unittest.TestCase):

    EVENTS = '#/events'
    CLIENTS = '#/clients'
    CHECKS = '#/checks'
    SILENCED = '#/silenced'
    STASHES = '#/stashes'
    AGGREGATES = '#/aggregates'
    DATACENTERS = '#/datacenters'

    def _generate_url(self):
        self.url_events = '{url}{rest}'.format(
            url=self.url,
            rest=self.EVENTS
        )
        self.url_clients = '{url}{rest}'.format(
            url=self.url,
            rest=self.CLIENTS
        )
        self.url_checks = '{url}{rest}'.format(
            url=self.url,
            rest=self.CHECKS
        )
        self.url_silenced = '{url}{rest}'.format(
            url=self.url,
            rest=self.SILENCED
        )
        self.url_stashes = '{url}{rest}'.format(
            url=self.url,
            rest=self.STASHES
        )
        self.url_aggregates = '{url}{rest}'.format(
            url=self.url,
            rest=self.AGGREGATES
        )
        self.url_datacenters = '{url}{rest}'.format(
            url=self.url,
            rest=self.DATACENTERS
        )

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.username = 'operator'
        self.password = 'changeme'
        self.ip = '192.168.1.64'
        self.url = 'https://{user}:{passw}@{ip}/uchiwa/'.format(
            user=self.username,
            passw=self.password,
            ip=self.ip
        )
        self._generate_url()

    def _url_load(self, url):
        driver = self.driver
        driver.get(url)
        sleep(2)
        return driver

    def _url_test(self, url, text):
        driver = self._url_load(url)
        assert text in driver.title

    def test_uchiwa_login(self):
        self._url_test(self.url, 'Events | Uchiwa')

    def test_uchiwa_events(self):
        self._url_test(self.url_events, 'Events | Uchiwa')

    def test_uchiwa_clients(self):
        self._url_test(self.url_clients, 'Clients | Uchiwa')

    def test_uchiwa_checks(self):
        self._url_test(self.url_checks, 'Checks | Uchiwa')

    def test_uchiwa_silenced(self):
        self._url_test(self.url_silenced, 'Silenced | Uchiwa')

    def test_uchiwa_stashes(self):
        self._url_test(self.url_stashes, 'Stashes | Uchiwa')

    def test_uchiwa_aggregates(self):
        self._url_test(self.url_aggregates, 'Aggregates | Uchiwa')

    def test_uchiwa_datacenters(self):
        self._url_test(self.url_datacenters, 'Datacenters | Uchiwa')

    def _uchiwa_search(self, text, items):
        driver = self._url_load(self.url_clients)
        self.assertIn("Clients", driver.title)
        elem = driver.find_element(By.XPATH,
                                   '//input[@ng-model=\'filters.q\']')
        elem.send_keys(text)
        sleep(1)
        search = driver.find_element_by_class_name('search-results')
        assert items in search.text

    def test_uchiwa_1_localhost(self):
        self._uchiwa_search('localhost', '1 Items')

    def test_uchiwa_3_overcloud(self):
        self._uchiwa_search('overcloud', '3 Items')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

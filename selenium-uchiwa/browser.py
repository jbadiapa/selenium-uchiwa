from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from time import gmtime
import sys


class Browser():

    def __init__(self,
                 username='admin',
                 password='admin',
                 protocol='http',
                 port=80,
                 ip='localhost',
                 wait=10,
                 screenshot_on_error=False):
        self.username = username
        self.password = password
        self.protocol = protocol
        self.port = port
        self.ip = ip
        self.wait = wait
        self.take_screenshot_on_error = screenshot_on_error

    def start(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver.implicitly_wait(self.wait)

    def set_url(self, base):
        if self.username is not None:
            user_password = '{}:{}@'.format(self.username,
                                            self.password)
            end = '/'
        else:
            user_password = ''
            end = ''

        self.url = '{protocol}://{u_p}{ip}:{port}/{base}{end}'.format(
            protocol=self.protocol,
            u_p=user_password,
            ip=self.ip,
            port=self.port,
            base=base,
            end=end)

    def take_screenshot(self):
        now = gmtime()
        self.driver.maximize_window()
        self.driver.save_screenshot('wait-{y}-{m}-{d}-{h}:{mi}:{s}.png'.format(
            y=now.tm_year,
            m=now.tm_mon,
            d=now.tm_mday,
            h=now.tm_hour,
            mi=now.tm_min,
            s=now.tm_sec
        ))

    def is_retry_exception(exception):
        return isinstance(
            exception,
            UnexpectedAlertPresentException)

    def is_retry_result(result):
        return result is None

    @retry(wait_fixed=1000, retry_on_exception=is_retry_exception)
    def find_element_css(self, selector, not_found=None):
        try:
            obj = self.driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            if self.take_screenshot_on_error:
                self.take_screenshot()
            return not_found
        return obj

    @retry(wait_fixed=1000, retry_on_result=is_retry_result,
           stop_max_attempt_number=5)
    def wait_for_obj(self, presence, timeout=10):
        try:
            elem = WebDriverWait(self.driver, timeout).until(presence)
            return elem
        except Exception:
            if self.take_screenshot_on_error:
                self.take_screenshot()
            return None

    def load_page(self, page):
        self.driver.get(page)

    def load_page_site(self, location):
        self.driver.get('{url}{location}'.format(
            url=self.url,
            location=location
        ))

    def parse_arguments(self):
        arguments = {'--ip': self.ip,
                     '--protocol': self.protocol,
                     '--username': self.username,
                     '--password': self.password,
                     '--port': self.port,
                     '--wait': self.wait}

        iterations = list(sys.argv)
        for arg in iterations:
            if arg in arguments.keys():
                pos = sys.argv.index(arg)
                sys.argv.pop(pos)
                arguments[arg] = sys.argv.pop(pos)

        self.ip = arguments['--ip']
        self.username = arguments['--username']
        self.password = arguments['--password']
        self.protocol = arguments['--protocol']
        self.port = arguments['--port']
        self.wait = arguments['--wait']

    def end(self):
        self.driver.close()

#!/bin/python

import sys
from selenium import webdriver


class FacebookLogin(object):

    def __init__(self, driver):
        """The html tag ids are all hard-coded, but could be changed
        to use args or kwargs. Supplying a different form id
        could allow use for any site.

        Using the login form to select email and password
        elements is not really necessary.
        I used it here for clarity and security.
        """

        self.driver = driver
        self.login_form = self.driver.find_element_by_id('login_form')
        self.user_box = self.login_form.find_element_by_id('email')
        self.pass_box = self.login_form.find_element_by_id('pass')
        self.username = None
        self.password = None

    def _check_element(self, e):
        """Check that the login form is visible.
        We don't want to enter our info into a hidden form.
        """

        name = e.get_attribute('name') or e.get_attribute('id')
        print 'checking: ', name
        print 'is visible', e.is_displayed()
        if e.get_attribute('type') == 'hidden':
            return False
        elif 'hidden' in e.get_attribute('class'):
            return False
        elif 'hidden' in e.get_attribute('style'):
            return False
        elif e.is_displayed():
            return True
        else:
            return True

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def _check_elements(self):
        if self._check_element(self.login_form):
            if self._check_element(self.user_box):
                if self._check_element(self.pass_box):
                    self.all_green = True
    def login(self):
        """check that user and pass are set, then check
        that each element is visible to the user.
        Then do login.
        """

        self._check_elements()
        print 'all green: ', self.all_green
        print 'starting login'
        if self.all_green:
            print 'all checks passed'
            self.user_box.clear()
            self.user_box.send_keys(self.username)
            self.pass_box.clear()
            self.pass_box.send_keys(self.password)
            self.login_form.submit()


def main():

    # setup selenium
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")

    username = sys.argv[1]
    password = sys.argv[2]

    facebook = FacebookLogin(driver)
    facebook.set_username(username)
    facebook.set_password(password)

    facebook.login()

    # can now access facebook.driver for further testing


if __name__ == '__main__':
    main()

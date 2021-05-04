#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Chrome Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument('--disable-gpu')  # Last I checked this was necessary.
CHROME_OPTIONS.add_argument('--disable-notifications')
prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
CHROME_OPTIONS.add_experimental_option('prefs', prefs)
CHROME_OPTIONS.add_argument('--ignore-certificate-errors')
CHROME_OPTIONS.add_argument("--test-type")
CHROME_OPTIONS.add_argument('--disable-infobars')
CHROME_OPTIONS.add_argument('--disable-extensions')
CHROME_OPTIONS.add_argument('--profile-directory=Default')
CHROME_OPTIONS.add_argument('--incognito')
CHROME_OPTIONS.add_argument('--disable-plugins-discovery')
CHROME_OPTIONS.add_argument('--start-maximized')

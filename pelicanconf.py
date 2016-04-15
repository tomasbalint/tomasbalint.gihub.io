#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom\xe1\u0161 B\xe1lint'
SITENAME = u'Energy Markets & Data Analysis'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('home','http://tomasbalint.com'),
    ('envelope','mailto:tomas.balint@gmail.com'),
    ('linkedin-square','https://www.linkedin.com/in/tomasbalint'),
    ('twitter-square', 'https://twitter.com/tomasbalint'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="pure-single"
STATIC_PATHS=['images']

# MY CONFIG - for the Pelican Pure theme
PROFILE_IMG_URL='images/TB_profile.jpg'

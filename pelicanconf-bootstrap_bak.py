#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom\xe1\u0161 B\xe1lint, Ph.D.'
SITENAME = u'TomasBalint.com'
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
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = None

# Social widget
SOCIAL = (
    ('Vitae','https://www.linkedin.com/in/tomasbalint', 'linkedin'),
    ('Tweets', 'https://twitter.com/tomasbalint', 'twitter'),
    ('Code','http://github.com/TomasBalint', 'github'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="themes/pelican-bootstrap3"
STATIC_PATHS=['images']
RELATIVE_URLS = True # set relative URLs links - mainly because of images
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_NAVBAR_INVERSE = False


ABOUT_ME = '''
Energy Markets, Climate Policy &amp; Data Analysis <br/><br/>
Postdoctoral researcher at <a href='http://centredeconomiesorbonne.univ-paris1.fr'>Centre d'Économie de la Sorbonne</a>,&nbsp;<br/>
<a href='http://www.univ-paris1.fr/'>Université Paris 1 Panthéon-Sorbonne</a>
'''
AVATAR = '/images/TB_profile.jpg'

BANNER = '/images/banner.png'
BANNER_TITLE = ''
BANNER_SUBTITLE = ''
BANNER_ALL_PAGES = True
HIDE_SITENAME = True

CC_LICENSE = "CC-BY-NC-SA"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# index page for all blog posts:
INDEX_SAVE_AS = '/pages/notes.html'
MENUITEMS = (
    ('HOME','/'),
    ('PROJECTS','/pages/projects.html'),
    ('VITAE','/pages/vitae.html'),
    ('NOTES','/pages/notes.html'),
)


# TWITTER TIMELINE
TWITTER_USERNAME = 'tomasbalint'
TWITTER_WIDGET_ID = '730363857198297088'

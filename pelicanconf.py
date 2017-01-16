#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom\xe1\u0161 B\xe1lint, Ph.D.'
SITENAME = u'Tomáš Bálint'
SITEURL = 'http://tomasbalint.com'


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
    ('E-mail','mailto:tomas@tomasbalint.com','envelope'),
    ('LinkedIn','https://www.linkedin.com/in/tomasbalint', 'linkedin'),
    ('Tweets', 'https://twitter.com/tomasbalint', 'twitter'),
    ('Code','https://github.com/TomasBalint', 'github'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="themes/pelican-bootstrap3"
STATIC_PATHS=['images']
RELATIVE_URLS = True # set relative URLs links - mainly because of images
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_NAVBAR_INVERSE = False

FAVICON='images/favicon.ico'


ABOUT_ME = '''
<strong>Energy Markets, Climate Policies &amp; Data Analysis</strong><br/><br/>
Postdoctoral researcher at <a href='http://centredeconomiesorbonne.univ-paris1.fr'>Centre d'Économie de la Sorbonne</a>,&nbsp;<br/>
<a href='http://www.univ-paris1.fr/'>Université Paris 1 Panthéon-Sorbonne</a><br/>
'''
AVATAR = '/images/Tomas-Balint.jpg'

#BANNER = '/images/banner.png'
#BANNER_TITLE = ''
#BANNER_SUBTITLE = ''
#BANNER_ALL_PAGES = True
HIDE_SITENAME = True

CC_LICENSE = "CC-BY-NC-SA"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# TB: my variable to show/hide archive link. By default archive is shown, i.e. HIDE_ARCHIVE = False
# N.B.: it removes the link to archives in the header, but does not disable the generation of archive.html page
HIDE_ARCHIVE = True

# TB: if you disable Sidebar you have displayed lite social media plugin programmed by myself. You can not use any other plugins that reside in the full sidebar.
HIDE_SIDEBAR = True

# index page for all blog posts:
INDEX_SAVE_AS = '/pages/notes.html'
MENUITEMS = (
    ('HOME','/'),
    ('VITAE','/pages/vitae.html'),
    ('RESEARCH','/pages/research.html'),
    ('CONTACT','/pages/contact.html'),
#    ('NOTES','/pages/notes.html'),
)


# TWITTER TIMELINE
#TWITTER_USERNAME = 'tomasbalint'
#TWITTER_WIDGET_ID = '730363857198297088'

# GOOGLE ANALYTICS
GOOGLE_ANALYTICS = 'UA-64046980-3'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS=['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# provides the info about social profiles for SEO purposes
# hardcoded
SOCIAL_MEDIA_SEARCH_CONNECTION = True
SOCIAL_LINK = "http://tomasbalint.com"
SOCIAL_TWITTER = "https://twitter.com/tomasbalint"
SOCIAL_GITHUB = "https://github.com/TomasBalint"
SOCIAL_LINKEDIN = "https://www.linkedin.com/in/tomasbalint"

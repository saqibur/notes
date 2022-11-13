AUTHOR = 'Saqibur Rahman'
SITENAME = "Saqibur's Notes"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Dhaka'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My customized settings
THEME = "theme"
OUTPUT_PATH = 'docs/'
LOAD_CONTENT_CACHE = False
PLUGINS = ['series']
SUMMARY_END_SUFFIX = '…'


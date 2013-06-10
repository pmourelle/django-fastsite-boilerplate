# Django settings for my_fastsite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'my_fastsite.db',
    }
}

#MEDIA_ROOT = ''
#MEDIA_URL = ''
#STATIC_ROOT = ''
#STATIC_URL = '/static/'

from settings_local import *

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'es-ES'
SITE_ID = 1
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/public/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '37%=g)niy5ln!9q6-*l%u3k)n7b5h@ez4n=_uk9w-oifo_fdl$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'luciernaga.pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS=(
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "luciernaga.context.variables",
    )

ROOT_URLCONF = 'luciernaga.urls'

TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',    
    'django.contrib.admin',
    'luciernaga.multimedia',
    'luciernaga.red',
    'luciernaga.material',
    'luciernaga.proyectos',
    'luciernaga.eventos',
    'south',
    'luciernaga.djcaptcha',
    'luciernaga.pagination',
    'haystack',
)

HAYSTACK_SITECONF = 'luciernaga.search_sites'
HAYSTACK_SEARCH_ENGINE = 'simple'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

AUTH_PROFILE_MODULE = 'red.Perfil'
RECAPTCHA_PUB_KEY = "6LdQgMASAAAAAMqmmS8ENSuxIP-D0FTaSBB6xtXF"
RECAPTCHA_PRIVATE_KEY = "6LdQgMASAAAAAG0HDB7DBoXWDBd8GYKSIsMzPUZQ"

CAPTCHA_BACKGROUND_COLOR = '#c3f5cc'
CAPTCHA_FOREGROUND_COLOR = '#000000'

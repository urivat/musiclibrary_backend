# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_d9**zl%u^xl$@*qcln+!y@k*stj=5wy^3(nd$g4)xc2bys1wz'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_database',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'password',
        'OPTIONS': {
            'autocommit': True
        }
    }
}


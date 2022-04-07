# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+@_sm8glf-yj)@z1d^wv+(42#-bj3^czi6cpcv3$o$h3c($bu7'

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


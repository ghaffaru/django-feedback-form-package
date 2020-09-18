=====================
Feedback Form Package
=====================

Feedback form package is a Django app to create and handle feedback forms on your website without writing it out yourself. Cheers


Quick start
-----------

1. Add "feedback" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'feedback',
    ]

2. Include the feedback URLconf in your project urls.py like this::

    path('feedback/', include('feedback.urls')),


3. Make sure to configure your email service in settings.py. Eg using sendgrid::

    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'apikey'
    EMAIL_HOST_PASSWORD = 'xxxxxxx' # Your key here
    EMAIL_USE_TLS = True

4. Indicate where to send email from and to, in your settings.py like so::

    EMAIL_TO = 'xxx@gmail.com'
    EMAIL_FROM= 'ghaff@gmail.com' # Connected to the mail service

5. Start the development server::

    ./manage.py runserver

6. Visit http://127.0.0.1:8000/feedback/
   to create see the glory. Dont mind the UI, this is v1, haha.

## Feedback Form Package
> A django app/package to create and handle feedback forms on website with minimal config

## Installation
Use [pip](https://pypi.org) to set it up

```
pip install django-feedback-form-package
```

## Usage
1. Add "feedback" to your INSTALLED_APPS in settings.py like so
```
INSTALLED_APPS = [
    ...
    'feedback'
]
```

2. Include the feedback URLconf in your project urls.py like so
```
path('feedback/', include('feedback.urls'))
```

3. Make sure to configure your email service in settings.py . Eg using sendgrid
```
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey' # Your api key name
EMAIL_HOST_PASSWORD = 'xxxxxx' # Your api key 
EMAIL_USE_TLS = True
```

4. Indicate where to send email from and to, in your settings.py like so
```
EMAIL_TO = 'xxx@gmail.com'
EMAIL_FROM = 'ghaff@gmail.com' # connected to the mail service
```

5. Start the development server
```
./manage.py runserver
```

6. Visit the URL
```
http://127.0.0.1/feedback
```
to see the glory. Dont mind the UI. This is v1. hahah

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
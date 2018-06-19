from flask import Flask
from django.apps import apps
from django.conf import settings
from poc import settings as my_settings
import django

settings.configure()
settings.DATABASES = my_settings.DATABASES
apps.populate(my_settings.INSTALLED_APPS)
django.setup()
app = Flask(__name__)

from app_poc.models import Hit


@app.route("/")
def index():
    # return str(5)
    print('inside index')
    return str(Hit.objects.count())


if __name__ == '__main__':
    app.run(debug=True)

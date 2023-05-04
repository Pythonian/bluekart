import os
from celery import Celery

# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# creates an instance of the application
app = Celery('config')

# load custom configuration from project settings
# All celery-related configuration keys should have CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover asynchronous tasks by celery
app.autodiscover_tasks()
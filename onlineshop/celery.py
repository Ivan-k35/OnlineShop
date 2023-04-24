import os
from celery import Celery

# set the default django settings module for 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop.settings')
app = Celery('onlineshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

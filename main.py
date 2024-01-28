# scraper_script.py
from project.maths import add
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
app = Celery('core')

# Set Redis as the broker
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'rpc://'
app.autodiscover_tasks(['project'])
# Explicitly set the broker to use Redis
app.conf.broker = 'redis://localhost:6379/0'


app.conf.beat_schedule = {
    'add_task': {
        'task': 'project.maths.search_job',  # Replace with your actual periodic task
        #'schedule':crontab(hour=12,minute=00,day_of_week=0)
        'schedule': timedelta(days=3),  # Adjust the schedule as needed
    },
}

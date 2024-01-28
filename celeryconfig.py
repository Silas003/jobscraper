# celeryconfig.py
from datetime import timedelta
broker_url = 'redis://localhost:6379/0'
result_backend = 'rpc://'


# 
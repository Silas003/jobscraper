
from project.maths import add,search_job

def new_task():
    print( 'running celery...')
    search_job.delay('backend')


new_task()
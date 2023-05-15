from celery import shared_task


@shared_task(name="task.add")
def add():
    return 2+2


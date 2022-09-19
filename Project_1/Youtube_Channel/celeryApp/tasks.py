from celery import shared_task
import time


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def sum(self, a,b):
    time.sleep(10)
    return a + b


@shared_task
def send_mail(email):
    print(f'A sample message is sent to {email}')
"""
    This file contains the tasks of API requests(e.g. start machine) to be put into task queue.
    Celery app (djcelery) will automatically scan the tasks file.
"""
from celery import task

# test function, simply return a sum of x and y
@task()
def add(x, y):
    return x+y
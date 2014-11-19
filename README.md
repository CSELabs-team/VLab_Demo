NYU CSE labs VLab Project Demo
Target of this project: Implement a centralized controlling system for the V-Lab virtual machines as well as an
interface for clients(students).

Developers: 
	Luming Nie
	Pujitha Gade
	Swetha Chauah

This repository dose not have settings.py file which should be setup in production environment respectively.
Required libraries are recorded in "requirements.txt" and can be "pip installed" to production environment.


Temporary Documentation:
Technology Stacks:
    1. Base:
        Django 1.6
        Python 2.7
        MySQL
        Oauth2.0(NYU Gmail account)
        VNC
        javascript
        Bootstrap
    2. Third Party Libraries:
        REST framework
        requests
        python-social-auth
    3. Task Queue:
        Celery.py + RabbitMQ

Project Structure:
    # to be completed

References:
1.Steps to setup Django-Celery in project:
    http://docs.celeryproject.org/en/2.5/django/first-steps-with-django.html
2.Rest framework documentation:
    http://www.django-rest-framework.org

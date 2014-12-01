NYU CSE labs VLab Project Demo <br>
Target of this project: Implement a centralized controlling system for the V-Lab virtual machines as well as an
interface for clients(students).  <br> <br>

<br>

Developers: <br>
&emsp;&emsp; Luming Nie <br>
&emsp;&emsp; Pujitha Gade <br>
&emsp;&emsp; Swetha Chauah <br>

<br>

This repository dose not have settings.py file which should be setup in production environment respectively. <br>
Required libraries are recorded in "requirements.txt" and can be "pip installed" to production environment. <br>

<br>

Temporary Documentation:
Technology Stacks: <br>
    1. Base: <br>
&emsp;&emsp; Django 1.6 <br>
&emsp;&emsp; Python 2.7 <br>
&emsp;&emsp; MySQL <br>
&emsp;&emsp; Oauth2.0(NYU Gmail account) <br>
&emsp;&emsp; VNC <br>
&emsp;&emsp; javascript <br>
&emsp;&emsp; Bootstrap <br>
    2. Third Party Libraries: <br>
&emsp;&emsp; REST framework <br>
&emsp;&emsp; requests <br>
&emsp;&emsp; python-social-auth <br>
    3. Task Queue: <br>
&emsp;&emsp; Celery.py + RabbitMQ <br>
    4. SSH Remote Execution: <br>
&emsp;&emsp; Paramiko Library (for executing remote bash scripts on computing nodes)

<br>

Project Structure: <br>
    # to be completed <br>

<br>

References: <br>
1.Steps to setup Django-Celery in project: <br>
&emsp;&emsp; http://docs.celeryproject.org/en/2.5/django/first-steps-with-django.html <br>
2.Rest framework documentation: <br>
&emsp;&emsp; http://www.django-rest-framework.org <br>

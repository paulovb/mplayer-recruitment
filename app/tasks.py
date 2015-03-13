from __future__ import absolute_import
from django.core.mail import send_mail

from celery import shared_task

@shared_task
def send_mail_queue(from_email, to_emails, subject, message):
    send_mail(subject, message, from_email, to_emails, fail_silently=False)
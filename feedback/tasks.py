from celery.decorators import task
from celery.utils.log import get_task_logger
from PIL import Image
from amazon import AmazonTask
from feedback.emails import send_feedback_email
import boto
import boto.s3
import sys
from boto.s3.key import Key
import os
from django.conf import settings
logger = get_task_logger(__name__)

@task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)

#AWS_STORAGE_BUCKET_NAME='development-branch'
#SECRET_KEY='A long string with many different types of characters'
           
@task()
def amazon_uploader():
    
    worker = AmazonTask(settings.AWS_S3_ACCESS_KEY_ID,settings.AWS_S3_SECRET_ACCESS_KEY,settings.AWS_STORAGE_BUCKET_NAME,settings.SECRET_KEY)  
    # implement file upload-section here.

    worker.upload_image(file_name,file_key,path)
    
@task()
def system_l():
    worker = AmazonTask(settings.AWS_S3_ACCESS_KEY_ID,settings.AWS_S3_SECRET_ACCESS_KEY,settings.AWS_STORAGE_BUCKET_NAME,settings.SECRET_KEY)  
    # implement file upload stuff here as well. :)
    worker.create_thumb_file(src_file,file_key,path,size)
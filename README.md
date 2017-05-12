## Django-Celery
 
Django celery is used for Asynchronous web, Developer can add multiple workers/tasks can execute simultanioulsy without making any delay for user to wait for any task.   

## Code Example

Following is the Example of Task you can add in your tasks.py file. You can define tasks.py file in each of your app's directory.

@task()
def amazon_uploader():
    worker = AmazonTask(settings.AWS_S3_ACCESS_KEY_ID,settings.AWS_S3_SECRET_ACCESS_KEY,settings.AWS_STORAGE_BUCKET_NAME,settings.SECRET_KEY)  
worker.upload_image(file_name,file_key,path)

## Motivation

This small project is inspired when I was working on Django Live Trading boat where I had to run various worker in the Backgroud. 

## Installation

pip install django
pip install django-celery

## Run project
Go to url: http://localhost:8000/feedback/

## Run Django

cd /project-directory
python manage.py runserver 
  

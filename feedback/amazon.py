#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:27:28 2017
@author: metal-machine
"""
import boto
import boto.s3
class AmazonTask(object):
 
    def __init__(self,amazon_ID,amazon_key,bucket_name,secret_key):
        self.amazon_ID=amazon_ID
        self.amazon_key=amzon_key
        self.bucket_name=bucket_name
        self.secret_key=secret_key
        	
    def upload_image(self,file_name,file_key,path):
        conn=boto.connecet_s3(self.amazon_id,self.aws_secret)
        bucket=conn.get_bucket(self.bucket_name)
        k=Key(bucket)
        full_key_name = os.path.join(path,file_key)
        k=bucket.new_key(full_key_name)
        return k.set_contents_from_filename(file_name)
        
    def create_thumb_file(self,src_file,file_key,path,size):
        conn = boto.connecet_s3(self.amazon_id,self.aws_secret)
        bucket = conn.get_bucket(self.bucket_name)
        conn = boto.connect_s3(settings.AWS_S3_ACCESS_KEY_ID,
                                settings.AWS_S3_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(self.bucket_name)
        k = Key(bucket)
        im = Image.open(src_file)
        im.thumbnail(size)
        im.save(src_file + ".thumbnail", "JPEG")
        full_key_name = os.path.join(path,file_key)
        k = bucket.new_key(full_key_name)
        return k.set_contents_from_filename(src_file + ".thumbnail")
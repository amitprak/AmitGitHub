import boto3 
import time
from boto3 import client
import re
import os
import sys


TODAYDATE = time.strftime('%Y%m%d') # Today's date in YYYYMMDD format.


s3 = boto3.client('s3')

client = boto3.client('sns')

def Email_Trigger( FILE_NAME_PREFIX):
    response = client.publish(
    TopicArn='arn:aws:sns:us-east-1:125810979284:Today_File_Present_Check',  
    Message='This is a late sub alert mail for  ' + FILE_NAME_PREFIX + ' file,Pls contact with source',
    Subject= 'Late Sub Alert For: ' +  FILE_NAME_PREFIX + ' File'
    )
    print ("Email Sent")
    


def lambda_handler(event, context):
     ALL_FILE_NAME =''
     FILE_NAME_PARAMETER = os.environ.get("FILE_NAME_PARAMETER")
     FILE_NAME_PREFIX = FILE_NAME_PARAMETER + TODAYDATE  # Concat Today's date after file name.
     for key in s3.list_objects(Bucket='amitfirsts3')['Contents']:
         FULL_FILE_NAME = (key['Key'])   # FULL_FILE_NAME variable will store full file name from S3 bucket.
         ALL_FILE_NAME =  ALL_FILE_NAME + FULL_FILE_NAME
         

     if re.search(FILE_NAME_PREFIX,ALL_FILE_NAME): # Checking BONY_SEC_YYYYMMDD is present or not in all the file name in s3
           print("File:" + FILE_NAME_PREFIX + " is present")
     else:
           Email_Trigger(FILE_NAME_PREFIX)










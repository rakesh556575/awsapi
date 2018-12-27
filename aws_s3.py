import os
from boto3 import client
import string
import random

class S3():
    """Example class demonstrating operations on S3"""

    bucket_name = "defaultbucket"

    def __init__(self, *args, **kwargs):
        """
        Initiazizing S3 object
        :param args: postional aruguments
        :param kwargs: key word arguments
        """
        region = kwargs.get('region_name', 'us-east-2')
        self.bucket_name = kwargs.get('bucket_name', self.bucket_name)
        self.s3client = client(
                                  's3',
                                  aws_access_key_id=kwargs.get("ACCESS_KEY","AKIAIKGNZUZEWBCVTXGA"),
                                  aws_secret_access_key=kwargs.get("SECRET_KEY","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"),

                          )

    def create_bucket(self):
        """
        Method to create a new bucket
        :return: Bucket name
        """


        while True:
            bucketName = self.randomNameGen()
            if self.bucket_exist(bucketName) is False:
                break

        try:
            
            self.s3client.create_bucket(Bucket=bucketName)

        except BaseException as e:
            return "Error occured beacuse of {}".format(e)


        return bucketName

    def randomNameGen(self,size=12):
        """
        Method to create a default size random string
        :param size:
        :return: random string
        """
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))


    def bucket_exist(self,bucketname):
        """
        Method to verify if bucket exists of not
        :param bucketname:
        :return: True or False if bucket exists
        """
        response = self.s3client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]

        return bucketname in buckets



from awsapi.awsapi.aws_s3 import S3


t1=S3(region_name="us-east-2",ACCESS_KEY="AKIAI7E3GPDFSQLWDPJA",SECRET_KEY="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")

bucket_name=t1.create_bucket()
print(bucket_name)



def test_aws_bucket_creation():
    t1 = S3(region_name="us-east-2", ACCESS_KEY="AKIAI7E3GPDFSQLWDPJA",
            SECRET_KEY="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")
    bucket_name = t1.create_bucket()
    assert t1.bucket_exist(bucket_name)==True
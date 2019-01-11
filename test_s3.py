from awsapi.awsapi.aws_s3 import S3


print("test1")


t1=S3(region_name="us-east-2",ACCESS_KEY="AKIAIKGNZUZEWBCVTXGA",SECRET_KEY="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")

bucket_name=t1.create_bucket()
print(bucket_name)



def test_aws_bucket_creation():
    t1 = S3(region_name="us-east-2", ACCESS_KEY="AKIAIKGNZUZEWBCVTXGA",
            SECRET_KEY="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")
    bucket_name = t1.create_bucket()
    assert t1.bucket_exist(bucket_name)==True

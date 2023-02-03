import boto3

ssm_client = boto3.client(
    "ssm",
    region_name="us-east-1",
    aws_access_key_id="9iBr11Rw0PE5Q65qZk2K6d8",
    aws_secret_access_key="/AKIAVC 9iBr11Rw0PE5Q65qZk2K6d8GC5HR8K5ZXBVGH"
)
print(ssm_client)

# standard string
# new_string_parameter = ssm_client.put_parameter(
#     Name='REST',
#     Description='Encryption Test parameter',
#     Value='DEMO@POP',
#     Type='SecureString',
#     Overwrite=True,
#     Tier='Standard',
#     DataType='text',

# )

get_response = ssm_client.get_parameter(
    Name='EncryptionTest',
    WithDecryption=True
)

# encrypted string
new_string_parameter = ssm_client.put_parameter(
    Name='EncryptionTest',
    Description='Encryption Test parameter',
    Value='test1234@123',
    Type='SecureString',
    Overwrite=True,
    Tier='Standard',
    DataType='text',

)

get_response = ssm_client.get_parameter(
    Name='EncryptionTest',
    WithDecryption=True
)

print(get_response["Parameter"]["Value"])
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import boto3
from decouple import config

bucket_name = config('BUCKET_NAME')

def extract():
    '''
    Function to extract the data from the parquet added to the S3 bucket and return a pandas dataframe
    '''
    s3 = boto3.client('s3',
                    aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))

    objects = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in objects:
        objects_sorted = sorted(objects['Contents'], key=lambda x: x['LastModified'], reverse=True)

        last_parquet = objects_sorted[0]['Key']
        print(f"O último arquivo adicionado ao bucket '{bucket_name}' é: {last_parquet}")
    else:
        print(f"O bucket '{bucket_name}' está vazio.")

 
    response = s3.get_object(Bucket=bucket_name, Key=last_parquet)

    parquet_content = response['Body'].read()

    parquet_table = pq.read_table(pa.BufferReader(parquet_content))
    extracted = parquet_table.to_pandas()

    return extracted
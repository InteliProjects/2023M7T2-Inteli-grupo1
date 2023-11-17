import os
from dotenv import load_dotenv
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import boto3
import copy
import numpy as np
import gc
import asyncio
import psycopg2

load_dotenv()

loop = asyncio.get_event_loop()

bucket_name = os.getenv('BUCKET_NAME')

def extract(file_name):
    aircraft_serial_number = None
    '''
    Function to extract the data from the parquet added to the S3 bucket and return a pandas dataframe
    '''
    s3 = boto3.client('s3',
                    aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY'))

   #  objects = s3.list_objects_v2(Bucket=bucket_name)

   #  if 'Contents' in objects:
   #      objects_sorted = sorted(objects['Contents'], key=lambda x: x['LastModified'], reverse=True)

   #      last_parquet = objects_sorted[0]['Key']

   #      aircraft_serial_number = last_parquet.split('_')[2]

   #      print(f"O último arquivo adicionado ao bucket '{bucket_name}' é: {last_parquet}")
   #  else:
   #      print(f"O bucket '{bucket_name}' está vazio.")

 
    response = s3.get_object(Bucket=bucket_name, Key=file_name)

    parquet_content = response['Body'].read()

    parquet_table = pq.read_table(pa.BufferReader(parquet_content))
    extracted = parquet_table.to_pandas()

    return extracted, aircraft_serial_number

methods = {
    'amscHprsovDrivF-1a': 'sum',
    'amscHprsovDrivF-1b': 'sum',
    'amscHprsovDrivF-2b': 'sum',
    'amscPrsovDrivF-1a': 'sum',
    'amscPrsovDrivF-1b': 'sum', 
    'amscPrsovDrivF-2b': 'sum',
    'basBleedLowPressF-1a': 'sum',
    'basBleedLowPressF-2b': 'sum',
    'basBleedLowTempF-1a': 'sum',
    'basBleedLowTempF-2b': 'sum',
    'basBleedOverPressF-1a': 'sum', 
    'basBleedOverPressF-2b': 'sum',
    'basBleedOverTempF-1a': 'sum', 
    'basBleedOverTempF-2b': 'sum',
    'bleedFavTmCmd-1a': 'mode', 
    'bleedFavTmCmd-1b': 'mode',
    'bleedFavTmCmd-2a': 'mode', 
    'bleedFavTmCmd-2b': 'mode', 
    'bleedFavTmFbk-1a': 'mode',
    'bleedFavTmFbk-1b': 'mode', 
    'bleedFavTmFbk-2b': 'mode', 
    'bleedHprsovCmdStatus-1a': 'sum',
    'bleedHprsovCmdStatus-1b': 'sum', 
    'bleedHprsovCmdStatus-2a': 'sum',
    'bleedHprsovCmdStatus-2b': 'sum', 
    'bleedHprsovOpPosStatus-1a': 'sum',
    'bleedHprsovOpPosStatus-1b': 'sum', 
    'bleedHprsovOpPosStatus-2a': 'sum',
    'bleedHprsovOpPosStatus-2b': 'sum', 
    'bleedMonPress-1a': 'mode',
    'bleedMonPress-1b': 'mode', 
    'bleedMonPress-2a': 'mode', 
    'bleedMonPress-2b': 'mode',
    'bleedOnStatus-1a': 'sum', 
    'bleedOnStatus-1b': 'sum', 
    'bleedOnStatus-2b': 'sum',
    'bleedOverpressCas-2a': 'sum', 
    'bleedOverpressCas-2b': 'sum',
    'bleedPrecoolDiffPress-1a': 'mean', 
    'bleedPrecoolDiffPress-1b': 'mean',
    'bleedPrecoolDiffPress-2a': 'mean', 
    'bleedPrecoolDiffPress-2b': 'mean',
    'bleedPrsovClPosStatus-1a': 'sum',
    'bleedPrsovClPosStatus-2a': 'sum',
    'bleedPrsovFbk-1a': 'sum',
    'bleedPrsovFbk-1b': 'sum',
    'bleedPrsovFbk-2b': 'sum',
    'message0418DAA-1': 'answer',
    'message0422DAA-1': 'answer',
}

# Separating the columns that are described in the TAP
columns_needed = ['amscHprsovDrivF-1a', 'amscHprsovDrivF-1b',
                'amscHprsovDrivF-2b', 'amscPrsovDrivF-1a',
                'amscPrsovDrivF-1b', 'amscPrsovDrivF-2b',
                'basBleedLowPressF-1a', 'basBleedLowPressF-2b',
                'basBleedLowTempF-1a', 'basBleedLowTempF-2b',
                'basBleedOverPressF-1a', 'basBleedOverPressF-2b',
                'basBleedOverTempF-1a', 'basBleedOverTempF-2b',
                'bleedFavTmCmd-1a', 'bleedFavTmCmd-1b',
                'bleedFavTmCmd-2a', 'bleedFavTmCmd-2b', 'bleedFavTmFbk-1a',
                'bleedFavTmFbk-1b', 'bleedFavTmFbk-2b', 'bleedHprsovCmdStatus-1a',
                'bleedHprsovCmdStatus-1b', 'bleedHprsovCmdStatus-2a',
                'bleedHprsovCmdStatus-2b', 'bleedHprsovOpPosStatus-1a',
                'bleedHprsovOpPosStatus-1b', 'bleedHprsovOpPosStatus-2a',
                'bleedHprsovOpPosStatus-2b', 'bleedMonPress-1a',
                'bleedMonPress-1b', 'bleedMonPress-2a', 'bleedMonPress-2b',
                'bleedOnStatus-1a', 'bleedOnStatus-1b', 'bleedOnStatus-2b',
                'bleedOverpressCas-2a', 'bleedOverpressCas-2b',
                'bleedPrecoolDiffPress-1a', 'bleedPrecoolDiffPress-1b',
                'bleedPrecoolDiffPress-2a', 'bleedPrecoolDiffPress-2b',
                'bleedPrsovClPosStatus-1a', 'bleedPrsovClPosStatus-2a',
                'bleedPrsovFbk-1a', 'bleedPrsovFbk-1b', 'bleedPrsovFbk-2b', 'message0418DAA-1', 'message0422DAA-1']

#Collumns that will be normalized
collums_normal = [
    'amscHprsovDrivF-1a',
    'amscHprsovDrivF-1b',
    'amscHprsovDrivF-2b',
    'amscPrsovDrivF-1a',
    'amscPrsovDrivF-1b', 
    'amscPrsovDrivF-2b',
    'basBleedLowPressF-1a',
    'basBleedLowPressF-2b',
    'basBleedLowTempF-1a',
    'basBleedLowTempF-2b',
    'basBleedOverPressF-1a', 
    'basBleedOverPressF-2b',
    'basBleedOverTempF-1a', 
    'basBleedOverTempF-2b',
    'bleedFavTmCmd-1a', 
    'bleedFavTmCmd-1b',
    'bleedFavTmCmd-2a', 
    'bleedFavTmCmd-2b', 
    'bleedFavTmFbk-1a',
    'bleedFavTmFbk-1b', 
    'bleedFavTmFbk-2b', 
    'bleedHprsovCmdStatus-1a',
    'bleedHprsovCmdStatus-1b', 
    'bleedHprsovCmdStatus-2a',
    'bleedHprsovCmdStatus-2b', 
    'bleedHprsovOpPosStatus-1a',
    'bleedHprsovOpPosStatus-1b', 
    'bleedHprsovOpPosStatus-2a',
    'bleedHprsovOpPosStatus-2b', 
    'bleedMonPress-1a',
    'bleedMonPress-1b', 
    'bleedMonPress-2a', 
    'bleedMonPress-2b',
    'bleedOnStatus-1a', 
    'bleedOnStatus-1b', 
    'bleedOnStatus-2b',
    'bleedOverpressCas-2a', 
    'bleedOverpressCas-2b',
    'bleedPrecoolDiffPress-1a', 
    'bleedPrecoolDiffPress-1b',
    'bleedPrecoolDiffPress-2a', 
    'bleedPrecoolDiffPress-2b',
    'bleedPrsovClPosStatus-1a',
    'bleedPrsovClPosStatus-2a',
    'bleedPrsovFbk-1a',
]

# Reduces the size of the dataframe by converting columns to smaller data types
def convert_columns(df_filtered):
    for column in df_filtered.columns:
        if df_filtered[column].dtype == 'float64':
            df_filtered[column] = df_filtered[column].astype('float32')

        if df_filtered[column].dtype == 'int64':
            df_filtered[column] = df_filtered[column].astype('int32')

    return df_filtered

# Agregation of the colunms based on the method
def process_column(col_name, method, dataframe):
    if method == 'max':
        return dataframe[col_name].max()
    elif method == 'sum':
        return dataframe[col_name].sum()
    elif method == 'answer':
        dataframe[col_name] = dataframe[col_name].apply(lambda x: 1 if x != 0 and pd.notnull(x) else 0)
        return dataframe[col_name].sum()
    elif method == 'mode':
        return dataframe[col_name].mode()[0]
    elif method == 'mean':
        return dataframe[col_name].mean()
    elif method == 'pass':
        return dataframe[col_name]
    else:
        raise ValueError(f"Unknown method {method} for column {col_name}")
    

# Function that agregates the data and normalize the data
def transformation(extracted, methods):
                # Select only the columns we need
                df = extracted.loc[:, columns_needed]
                # Reducing the data types to save memory
                df = convert_columns(df)

                count = len(df)
                
                # Summarizing the data and creating a new DataFrame with the results
                summary_data = copy.deepcopy({col: process_column(col, method, df) for col, method in methods.items()})

                
                df_output = pd.DataFrame([summary_data])

                # Creating a new colum called fightHours that receives COUNT
                df_output['flightMinutes'] = count * 50 / 60000
                
                # Cleaning up the memory
                del df
                gc.collect()

                # Selecting only the columns that will be normalized
                DF_NORMAL = df_output[collums_normal]

                # Normalizing the data
                DF_NORMAL = (DF_NORMAL - DF_NORMAL.min()) / (DF_NORMAL.max() - DF_NORMAL.min())
                DF_NORMAL = DF_NORMAL.fillna(0)

                # Replacing the columns with the normalized data
                df_output[collums_normal] = DF_NORMAL

                df_output.rename(columns=lambda x: x.replace("-", "_"), inplace=True)
                return df_output

# Loading the data into the database
async def loading(aircraft_serial_number, transformed):
   print(transformed.to_dict())
   #  db = Prisma(auto_register=True)

   #  await db.connect()

   #  airplane = None

   #  try:
   #    airplane = await db.airplane.find_first_or_raise(
   #             where={
   #                "aircraftSerNum_1": aircraft_serial_number
   #             },
   #          )
    
   #  except:
   #    airplane = await db.airplane.create(
   #      {
   #        "aircraftSerNum_1": aircraft_serial_number,
   #        "description": "None",
   #      }
   #    )
    
   #  flight = await db.flight.create(
   #      {
   #          "airplaneId": airplane.id
   #      }
   #  )

   #  transformed = await db.transformed.create(
   #      {
   #          "flightId": flight.id,
   #          "aircraftSerNum_1": aircraft_serial_number,
   #          **{col: float(transformed[col].iloc[0]) for col in transformed.columns}
   #      }
   #  )
    

   #  await db.disconnect()

   conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
   )
   cur = conn.cursor()

   # Tenta buscar a aeronave pelo número de série
   cur.execute(
      "SELECT id FROM airplane WHERE aircraftSerNum_1 = %s", 
      (aircraft_serial_number,)
   )
   airplane = cur.fetchone()

   # Se não encontrou, cria uma nova entrada para a aeronave
   if not airplane:
      cur.execute(
         "INSERT INTO airplane (aircraftSerNum_1, description) VALUES (%s, 'None') RETURNING id",
         (aircraft_serial_number,)
      )
      airplane_id = cur.fetchone()[0]
   else:
      airplane_id = airplane[0]

   # Cria um novo registro de voo para a aeronave
   cur.execute(
      "INSERT INTO flight (airplaneId) VALUES (%s) RETURNING id",
      (airplane_id,)
   )
   flight_id = cur.fetchone()[0]

   # Cria uma entrada transformada para o voo
   transformed_values = {
      "flightId": flight_id,
      "aircraftSerNum_1": aircraft_serial_number,
      **{col: float(transformed[col].iloc[0]) for col in transformed.columns}
   }
   columns = transformed_values.keys()
   values_placeholder = ', '.join(['%s'] * len(transformed_values))
   cur.execute(
      f"INSERT INTO transformed ({', '.join(columns)}) VALUES ({values_placeholder})",
      tuple(transformed_values.values())
   )

   # Fecha a conexão
   conn.commit()
   cur.close()
   conn.close()

   print("Dados carregados com sucesso!")


def lambda_handler(event, context):
   file_name = event['Records'][0]['s3']['object']['key']
   df, aircraft_serial_number = extract(file_name)
   new_df = transformation(df, methods)
   loop.run_until_complete(loading(aircraft_serial_number, new_df))

# asyncio.run(lambda_handler())
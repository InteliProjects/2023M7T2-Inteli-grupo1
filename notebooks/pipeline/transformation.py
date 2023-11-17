import pandas as pd
import numpy as np
import gc
import os
import copy

# Separating the columns that are described in the TAP
columns_needed = ['aircraftSerNum-1','amscHprsovDrivF-1a', 'amscHprsovDrivF-1b',
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



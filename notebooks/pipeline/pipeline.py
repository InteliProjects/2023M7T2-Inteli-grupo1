import extraction
import transformation
import loading

# Creating a dictionary to map the column names to the aggregation method names
methods = {
    'aircraftSerNum-1': 'pass',
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

# Extracting the data
extracted_data = extraction.extract()

# Transforming the data
transformed_data = transformation.transformation(extracted_data, methods)

# Loading the data
loading.loading(transformed_data)

print("Processo de ETL concluído com sucesso!")




import pandas as pd
from sqlalchemy import create_engine
from decouple import config

# Configuring the database connection
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_host = config('DB_HOST')
db_port = config('DB_PORT')
db_name = config('DB_NAME')

# Database connection
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Loading the data into the database
def loading(transformed):
    # print(transformed)
    
    airplane = pd.DataFrame({
        "aircraftSerNum_1": transformed["aircraftSerNum_1"],
        "decription": transformed["aircraftSerNum_1"],
    })
    airplane_info = airplane.to_sql('Airplane', con=engine, if_exists='replace', index=False)
    print("Ariplane infoo: ", airplane_info)
    
    flight = {
        ""
    }
    transformed[""].to_sql('Flight', con=engine, if_exists='append', index=False)
    
    
    
    transformed.to_sql('Transformed', con=engine, if_exists='append', index=False)

    engine.dispose()

    print("Dados carregados com sucesso!")
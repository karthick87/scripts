" Make sure that you have the following libraries installed on your machine
> pip install mysqlclient
> pip install pandas
> pip install sqlalchemy
"
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql://db_username:db_password@db_server_ip:db_server_port/db_name')
dframe = pd.read_sql_query('SELECT * FROM <table_name>', engine)
dframe.head()

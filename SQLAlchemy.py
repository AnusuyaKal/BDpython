from sqlalchemy import create_engine
import pandas as pd

hostname = 'ec2-3-9-191-104.eu-west-2.compute.amazonaws.com'
database = 'testdb'
username = 'consultants'
password = 'WelcomeItc@2022'
port_id = 5432

# Connect to Hive with SQLAlchemy
engine = create_engine('postgresql://consultants:WelcomeItc@2022@ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb')

# Execute SQL query to fetch data into DataFrame
sql_query = 'SELECT * FROM Anu_sqp1'
df = pd.read_sql(sql_query, engine)

# Close the SQLAlchemy engine
engine.dispose()

# Now you can work with the DataFrame 'df'
print(df.head())

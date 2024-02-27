import pandas as pd
import psycopg2

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/anusu/Documents/BDpython/Post_Gres3.csv')
print("dataframe",df)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="testdb",
    user="consultants",
    password="WelcomeItc@2022",
    host="ec2-3-9-191-104.eu-west-2.compute.amazonaws.com",
    port="5432"
)

# Create a cursor object using the cursor() method
cur = conn.cursor()

# # Define the SQL query to create the table (if it doesn't already exist)
# create_table_query = """
# CREATE TABLE IF NOT EXISTS your_table (
#     column1 datatype1,
#     column2 datatype2,
#     ...
# );
# """

# # Execute the SQL query to create the table
# cur.execute(create_table_query)

# Insert data into the table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO anu_sqp1 (name, age, salary)
    VALUES (%s, %s, %s);
    """
    cur.execute(insert_query, tuple(row))
    
# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

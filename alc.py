import psycopg2
import pandas as pd

# Database connection parameters
conn = psycopg2.connect(
    dbname="testdb",
    user="consultants",
    password="WelcomeItc@2022",
    host="ec2-3-9-191-104.eu-west-2.compute.amazonaws.com",
    port="5432")

# SQL query to fetch rows from a table
sql_query = 'SELECT * FROM anu_sqp1'

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        dbname="testdb",
        user="consultants",
        password="WelcomeItc@2022",
        host="ec2-3-9-191-104.eu-west-2.compute.amazonaws.com",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute(sql_query)

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Get column names from cursor description
    col_names = [desc[0] for desc in cur.description]

    # Create a DataFrame from the fetched rows and column names
    df = pd.DataFrame(rows, columns=col_names)

    # Print the DataFrame
    print(df)

except psycopg2.Error as e:
    print('Error connecting to the PostgreSQL database:', e)

finally:
    # Close the cursor and connection
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()

import psycopg2

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

# Define the SQL query to insert rows
sql = """
INSERT INTO anu_sqp1 (name, age, salary)
VALUES (%s, %s, %s);
"""

# Define the values to insert
values = [
    ('Sam',4,6000),
    #('value3', 'value4', ...),
    #...
]

# Execute the SQL query for each row of values
for row_values in values:
    cur.execute(sql, row_values)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

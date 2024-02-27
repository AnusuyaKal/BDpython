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

# Execute a SQL query
df = cur.execute("SELECT * FROM anu_sqp")

# Fetch all rows from the result set
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

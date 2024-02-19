import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('Zoo.db')

# Create a cursor object
c = conn.cursor()

# Create the Animal table
c.execute('''CREATE TABLE Animal
             (name text, species text)''')

# Insert three animals
c.execute("INSERT INTO Animal VALUES ('Lion', 'Mammal')")
c.execute("INSERT INTO Animal VALUES ('Tiger', 'Mammal')")
c.execute("INSERT INTO Animal VALUES ('Elephant', 'Mammal')")

# Commit the changes and close the connection
conn.commit()

# Read from the database and print the animals
c.execute("SELECT * FROM Animal")
rows = c.fetchall()

for row in rows:
    print(f"Name: {row[0]}, Species: {row[1]}")

# Close the connection
conn.close()

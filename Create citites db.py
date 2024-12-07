import sqlite3

def create_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()

    # Create the Cities table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cities (
        CityID INTEGER PRIMARY KEY,
        CityName TEXT NOT NULL,
        Population REAL NOT NULL
    )
    ''')

    # Add 20 cities to the table (From Minnesota)
    cities = [
        ("Minneapolis", 425115),
        ("St. Paul", 303820),
        ("Rochester", 122413),
        ("Duluth", 87680),
        ("Bloomington", 87398),
        ("Brooklyn Park", 82017),
        ("Woodbury", 79538),
        ("Plymouth", 77648),
        ("Lakeville", 76243),
        ("Blaine", 73774),
        ("Maple Grove", 71288),
        ("St. Cloud", 71013),
        ("Eagan", 67396),
        ("Burnsville", 64772),
        ("Coon Rapids", 63377),
        ("Eden Praire", 62166),
        ("Apple Valley", 55336),
        ("Edina", 53348),
        ("Minnetonka", 52463),
        ("St. Louis Park", 49697)
    ]

    # Insert the data into the table
    cursor.executemany('''
    INSERT INTO Cities (CityName, Population) VALUES (?, ?)
    ''', cities)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print("Database created and populated successfully.")

if __name__ == "__main__":
    create_database()

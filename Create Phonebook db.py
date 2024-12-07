import sqlite3

def create_phonebook():
    # Connect to (or create) the database
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Create the Entries table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Entries (
        Name TEXT PRIMARY KEY,
        PhoneNumber TEXT NOT NULL
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Phonebook database created successfully.")

if __name__ == "__main__":
    create_phonebook()

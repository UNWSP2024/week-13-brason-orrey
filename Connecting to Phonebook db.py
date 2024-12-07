import sqlite3

def add_entry(name, phone_number):
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)', (name, phone_number))
        conn.commit()
        print(f"Entry added: {name} - {phone_number}")
    except sqlite3.IntegrityError:
        print(f"Error: An entry for '{name}' already exists.")
    finally:
        conn.close()

def lookup_phone_number(name):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
    result = cursor.fetchone()
    if result:
        print(f"{name}'s phone number is {result[0]}")
    else:
        print(f"No entry found for '{name}'.")
    conn.close()

def update_phone_number(name, new_phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Entries SET PhoneNumber = ? WHERE Name = ?', (new_phone_number, name))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"{name}'s phone number updated to {new_phone_number}.")
    else:
        print(f"No entry found for '{name}'.")
    conn.close()

def delete_entry(name):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Entries WHERE Name = ?', (name,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Entry for '{name}' deleted.")
    else:
        print(f"No entry found for '{name}'.")
    conn.close()

def main():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Entry")
        print("2. Look Up Phone Number")
        print("3. Update Phone Number")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_entry(name, phone_number)
        elif choice == "2":
            name = input("Enter name to look up: ")
            lookup_phone_number(name)
        elif choice == "3":
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            update_phone_number(name, new_phone_number)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_entry(name)
        elif choice == "5":
            print("Exiting Phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

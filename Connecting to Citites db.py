import sqlite3

def display_cities_sorted(order_by, ascending=True):
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    order = 'ASC' if ascending else 'DESC'
    cursor.execute(f'''
    SELECT CityName, Population FROM Cities ORDER BY {order_by} {order}
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    conn.close()

def display_total_population():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(Population) FROM Cities')
    total = cursor.fetchone()[0]
    print(f"Total Population: {total}")
    conn.close()

def display_average_population():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(Population) FROM Cities')
    average = cursor.fetchone()[0]
    print(f"Average Population: {average}")
    conn.close()

def display_highest_population_city():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1')
    city = cursor.fetchone()
    print(f"City with Highest Population: {city[0]} ({city[1]})")
    conn.close()

def display_lowest_population_city():
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1')
    city = cursor.fetchone()
    print(f"City with Lowest Population: {city[0]} ({city[1]})")
    conn.close()

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Display cities sorted by population (ascending)")
        print("2. Display cities sorted by population (descending)")
        print("3. Display cities sorted by name")
        print("4. Display total population")
        print("5. Display average population")
        print("6. Display city with the highest population")
        print("7. Display city with the lowest population")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_cities_sorted("Population", ascending=True)
        elif choice == "2":
            display_cities_sorted("Population", ascending=False)
        elif choice == "3":
            display_cities_sorted("CityName", ascending=True)
        elif choice == "4":
            display_total_population()
        elif choice == "5":
            display_average_population()
        elif choice == "6":
            display_highest_population_city()
        elif choice == "7":
            display_lowest_population_city()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

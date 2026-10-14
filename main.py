
flights = [
    {"id": 103, "name": "IndiGo", "source": "Pune",
     "destination": "Delhi", "price": 4500},
    {"id": 101, "name": "Air India", "source": "Pune",
     "destination": "Mumbai", "price": 2500},
    {"id": 104, "name": "Akasa Air", "source": "Pune",
     "destination": "Bengaluru", "price": 3800},
    {"id": 102, "name": "SpiceJet", "source": "Pune",
     "destination": "Delhi", "price": 4200}
]

reservations = []


def display_flights(flight_list):
    print("\nAvailable Flights")
    print("-" * 65)

    for flight in flight_list:
        print(
            f"ID: {flight['id']} | "
            f"Airline: {flight['name']} | "
            f"{flight['source']} to {flight['destination']} | "
            f"Price: Rs.{flight['price']}"
        )


def search_flight(flight_id):
    # Linear Search
    for flight in flights:
        if flight["id"] == flight_id:
            return flight
    return None


def sort_flights_by_price():
    # Bubble Sort
    sorted_flights = flights.copy()
    n = len(sorted_flights)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_flights[j]["price"] > sorted_flights[j + 1]["price"]:
                sorted_flights[j], sorted_flights[j + 1] = (
                    sorted_flights[j + 1],
                    sorted_flights[j]
                )

    return sorted_flights


def book_flight():
    try:
        flight_id = int(input("Enter Flight ID to book: "))
    except ValueError:
        print("Please enter a valid numeric Flight ID.")
        return

    flight = search_flight(flight_id)

    if flight:
        passenger = input("Enter passenger name: ").strip()

        if not passenger:
            print("Passenger name cannot be empty.")
            return

        reservation = {
            "passenger": passenger,
            "flight": flight
        }
        reservations.append(reservation)

        print("\nReservation Successful!")
        print("Passenger:", passenger)
        print("Airline:", flight["name"])
        print("Route:", flight["source"], "to", flight["destination"])
        print("Ticket Price: Rs.", flight["price"])
    else:
        print("Flight ID not found.")


def view_reservations():
    if not reservations:
        print("\nNo reservations found.")
        return

    print("\nBooked Reservations")
    for reservation in reservations:
        flight = reservation["flight"]
        print(
            reservation["passenger"],
            "|", flight["name"],
            "|", flight["source"], "to", flight["destination"],
            "| Rs.", flight["price"]
        )


def main():
    while True:
        print("\n===== Flight Reservation System =====")
        print("1. Display Flights")
        print("2. Search Flight by ID")
        print("3. Sort Flights by Price")
        print("4. Book Flight")
        print("5. View Reservations")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_flights(flights)

        elif choice == "2":
            try:
                flight_id = int(input("Enter Flight ID to search: "))
                flight = search_flight(flight_id)

                if flight:
                    display_flights([flight])
                else:
                    print("Flight not found.")
            except ValueError:
                print("Please enter a valid numeric Flight ID.")

        elif choice == "3":
            sorted_flights = sort_flights_by_price()
            print("\nFlights Sorted by Price (Low to High)")
            display_flights(sorted_flights)

        elif choice == "4":
            book_flight()

        elif choice == "5":
            view_reservations()

        elif choice == "6":
            print("Thank you for using Flight Reservation System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

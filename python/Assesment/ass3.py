'''Transport Reservation System (Bus Ticketing)
Design a Python class BusReservation that simulates a basic bus ticket booking system.
Features should include:
➔ Show Available Routes:
● Predefined city routes with fixed prices.
● Example: "Mumbai to Pune - ₹500", "Delhi to Jaipur - ₹600", etc.
➔ Book Ticket:
● Enter passenger name, age, mobile, and route.
● Assign seat number (max 40 per bus per route).
● Generate a unique ticket ID.
➔ View Ticket:
● Lookup using ticket ID.
➔ Cancel Ticket:
● Cancel the ticket if it exists.
➔ Exit'''

 

class BusReservation:
    def __init__(self):         
        self.routes = {
            "Ahemdabad-Baroda": 300,
            "Dwarka-Jamnagar": 250,
            "Mumbai-Pune": 500,
            "Delhi-Jaipur": 600
        }
        self.booking = {}
        self.seats_per_route = {route: 0 for route in self.routes}
        self.ticket_id_counter = 1
        self.max_seats = 40

    # ---------------------------------------------------------------------------------------------------------------------
 
    def view_routes(self):
        print("\nAvailable Routes:")
        for route, price in self.routes.items():
            print(f"{route} - {price}")

    # -----------------------------------------------------------------------------------------------------------------

    def book_ticket(self):
        for route, price in self.routes.items():
            print(f"{route} - {price}")
        print("\nBook your tickets:")
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        mobile = input("Enter passenger mobile number: " )
        route = input("Enter your route: ")
        
        if route  in self.routes:
            if len(mobile) == 10 and mobile.isdigit():
                if self.seats_per_route[route] < self.max_seats:
                    ticket_id = self.ticket_id_counter
                    seat_no = self.seats_per_route[route] + 1

                    self.booking[ticket_id] = {
                        "name": name,
                        "age": age,
                        "mobile": mobile,
                        "route": route,
                        "seat_no": seat_no
                    }

                    self.seats_per_route[route] += 1
                    self.ticket_id_counter += 1

                    print(f"Your ticket is booked successfully! Ticket ID: {ticket_id}, Seat No: {seat_no}")
                else:
                     print("Sorry, this bus is fully booked!")
            else:
                print("Invalid mobile number!")
        else:
            print("No bus for this route.")

    #------------------------------------------------------------------------------------------------------------------    

    def view_ticket(self):
        
        tid = int(input("Enter ticket ID: "))
        if tid in self.booking:
            ticket = self.booking[tid]
            print("\nTicket Details:")
            print(f"Ticket ID: {tid}")
            print(f"Name     : {ticket['name']}")
            print(f"Age      : {ticket['age']}")
            print(f"Mobile   : {ticket['mobile']}")
            print(f"Route    : {ticket['route']}")
            print(f"Seat No  : {ticket['seat_no']}")
        else:
            print("Ticket not found.")

    #----------------------------------------------------------------------------------------------------------

    def cancel_ticket(self):
        
        tid = int(input("Enter ticket ID to cancel: "))
        if tid in self.booking:
            route = self.booking[tid]["route"]
            self.seats_per_route[route] -= 1
            self.booking.pop(tid)
            print("Ticket cancelled successfully.")
        else:
            print("Ticket ID not found.")

     # ----------------------------------------------------------------------------------------------------------------------------
    def run(self):
        while True:
            print("\n--- Bus Ticket Booking System ---")
            print("1. View Available Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")
           
            choice = int(input("Enter your choice: "))    
            match choice:
                    case 1:
                            self.view_routes()
                    case 2:
                            self.book_ticket()
                    case 3:
                            self.view_ticket()
                    case 4:
                            self.cancel_ticket()
                    case 5:
                            print("Thank you for visiting!")
                            break
                    case _:
                            print("Invalid choice! Please try again.")
                            print(choice, type(choice))
    
#---------------------------------------------------------------------------------------------------------------------
bus_system = BusReservation()
bus_system.run()

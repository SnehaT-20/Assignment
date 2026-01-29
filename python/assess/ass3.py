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

Routes={"Ahemdabad-Baroda":300,"Dwarka-Jamnagar":250,"Mumbai-Pune":500,"Delhi-Jaipur":600}
Booking={}
Seats_per_route = {route: 0 for route in Routes} 
Ticket_id = 1 
while True:
    
    print("\n---TICKET BOOKING SYSTEM ---")
    print("1. View Available Routes ")
    print("2. Booking Tickets")
    print("3. View Tickets")
    print("4. Cancel Tickets")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Available Routes lists:  ")
            for i,j in Routes.items():
                print(i,": ",j) 
        case 2:
            print("Book your tickets: ")
            name=input("Enter passenger name: ")
            age=int(input("Enter passenger age: "))
            mobile=input("Enter passenger number: ")
            route=input("Enter your route : ")
            if route in Routes:
                if len(mobile) == 10 and mobile.isdigit():
                    if Seats_per_route[route] < 40:   
                        Booking[Ticket_id] = {
                            "name": name,
                            "age": age,
                            "mobile": mobile,
                            "route": route,
                            "seat_no": Seats_per_route[route] 
                        }
                        Seats_per_route[route] += 1
                        print(f"Your ticket is booked successfully! Ticket ID: {Ticket_id}")
                        Ticket_id += 1
                    else:
                        print("Sorry, this bus is fully booked!")
                else:
                    print("Your mobile number is in invalid format")
            else:
                print("There is not any bus for this route...")
            Ticket_id+=1                 

        case 3:
            print("Your ticket: ")            
            tid=int(input("enter ticket id: "))
            if tid in Booking:
                s = Booking[Ticket_id]
                print("\n Tickets Details")
                print("ID:", Ticket_id)
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Mobile:", s["mobile"])
                print("Routes:", s["Routes"])
                print("Seat No:", s["seat_no"])

            else:
                print("Tickets is not found.")        

        case 4:
            print("cancel tickets: ")
            tid=int(input("enter student id: "))
            if tid in Booking:
                 Booking.pop(Ticket_id)
            print("cancel successfully")

        case 5:
            print("Thank you for visiting.....")
            break

        case _:
            print("may be your choice is invalid ....try again")

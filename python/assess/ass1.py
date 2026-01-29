'''Healthcare Industry
Design a Python class ClinicAppointment that manages patient appointments in a clinic.
The system should have the following features:
➔ Book Appointment:
● Prompt for patient name, age, mobile number, and preferred doctor.
● Show time slots (10am, 11am, 12pm, 2pm, 3pm).
● Check slot availability and confirm booking.
➔ View/Cancel Appointment:
● Allow patient to view or cancel their appointment using mobile number.
➔ Doctor Availability:
● Maintain a maximum of 3 appointments per time slot per doctor.
➔ Data Persistence:
● Store appointments in memory only (no files/dbs required).'''

# doctors and their slots
dr_dict={"dr. harmi" : {"10am":0,"11am":0},"dr. disha" : {"2pm":0,"3pm":0,"4pm":0}}

# appoinments stores here 
appointment={}
while True:
    
    print("--- Clinic Appointment System ---")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter patient name: ")
            age = input("Enter age: ")
            mobile = input("Enter mobile number: ")

            # Available doctors
            print(dr_dict.keys(),end=" ")
            doctor = input("Enter preferred doctor name: ")

            # Available doctor's slots
            print("Available Time Slots:")
            print(dr_dict[doctor],end=" ")
            sel_slot=input("enter select slot: ")

            # slots checking           
            if sel_slot not in dr_dict[doctor]:
                   print("Invalid slot.")
            elif dr_dict[doctor][sel_slot] >= 3:
                    print("Slot full! Choose another slot.")
            elif mobile in appointment:
                print("Appointment already exists for this mobile number.")
            else: 
                # storing appoinment if slots is full
                appointment[mobile] ={
                "name": name,
                "age": age,
                "doctor": doctor,
                "slot": sel_slot}            
                dr_dict[doctor][sel_slot] += 1
                print(f"{name} appointment is booked with {doctor} at {sel_slot}")          
                print(f"after booking slot {dr_dict[doctor]}")

        case 2:
            # check details based on mobile num 
            mobile = input("Enter mobile number: ")
            if mobile in appointment:
                app = appointment[mobile]
                print("\nAppointment Details")
                print("Name:", app["name"])
                print("Age:", app["age"])
                print("Doctor:", app["doctor"])
                print("Slot:", app["slot"])
            else:
                print("No appointment found.")
                 
        case 3:
            # remove appoinment based on mobile number and also free the space in doctore nd slot section
            mobile = input("Enter mobile number: ")
            if mobile in appointment:
                app = appointment[mobile]
                doctor = app["doctor"]
                slot = app["slot"]

                dr_dict[doctor][slot] -= 1
                del appointment[mobile]
                print("Appointment cancelled successfully.")
            else:
                print("No appointment found.")
        
        case 4:
            print("Thank you for visiting....")
            break
        case _ :
             print("Invalid choice! Please try again.")


    



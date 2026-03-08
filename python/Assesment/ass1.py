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

class ClinicAppointment:

    def __init__(self):
        self.dr_dict = {
            "dr. Mona": {"10am": 0, "11am": 0},
            "dr. Mohnish": {"2pm": 0, "3pm": 0, "4pm": 0}
        }
        self.appointment = {}

    # ---------------------------------------------------------------------------------------------------------------------
    def booking(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")

        for i in self.dr_dict:
         print(i)      #view dr and entering dr
        doctor = input("Enter preferred doctor name: ")

        print("Available Time Slots:")
        print(self.dr_dict[doctor])     # view slot and entering slot
        sel_slot = input("Enter select slot: ")

        if sel_slot  in self.dr_dict[doctor]:
            if self.dr_dict[doctor][sel_slot] <3:
                if mobile not in self.appointment:
                    self.appointment[mobile] = {
                            "name": name,
                            "age": age,
                            "doctor": doctor,
                            "slot": sel_slot 
                            }
                    self.dr_dict[doctor][sel_slot] += 1
                    print(f"{name} appointment is booked with {doctor} at {sel_slot}")
                    print(f"after booking slot {self.dr_dict[doctor]}")
                else:
                    print("Appointment already exists for this mobile number.")
            else:
                print("Slot full! Choose another slot.")
        else:
            print("Invalid slot.")

    # -------------------------------------------------------------------------------------------------------------------------
    def view(self):
        mobile = input("Enter mobile number: ")

        if mobile in self.appointment:
            app = self.appointment[mobile]
            print("\nAppointment Details")
            print("Name:", app["name"])
            print("Age:", app["age"])
            print("Doctor:", app["doctor"])
            print("Slot:", app["slot"])
        else:
            print("No appointment found.")

    # ------------------------------------------------------------------------------------------------------------------
    def cancel(self):
        mobile = input("Enter mobile number: ")

        if mobile in self.appointment:
            app = self.appointment[mobile]
            doctor = app["doctor"]
            slot = app["slot"]
            self.dr_dict[doctor][slot] -= 1
            del self.appointment[mobile]
            print("Appointment cancelled successfully.")
        else:
            print("No appointment found.")

    #-------------------------------------------------------------------------------------------------------------------------------------------
    def menu(self):
        while True:
            print("\n--- Clinic Appointment System ---")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    self.booking()
                case 2:
                    self.view()
                case 3:
                    self.cancel()
                case 4:
                    print("Thank you for visiting....")
                    break
                case _:
                    print("Invalid choice! Please try again.")

# ------------------------------------------------------------------------------------------------------------------------------
clinic = ClinicAppointment()
clinic.menu()

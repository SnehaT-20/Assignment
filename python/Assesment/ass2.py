'''School Management System
Design a Python class SchoolManagement that helps manage student admissions and
records. The system should support:
➔ New Admission:
● Collect student name, age, class (1-12), and guardian's mobile number.
● Assign a unique student ID automatically.
● Validate age: must be between 5 and 18.
● Validate mobile number: must be 10 digits.
➔ View Student Details:
● Allow lookup using student ID.
➔ Update Student Info:
● Update mobile number or class.
➔ Remove Student Record:
● Remove a student using their student ID.
➔ Exit System'''


class SchoolManagement:

    def __init__(self):
        self.admission = {}
        self.next_student_id = 1

    # -------------------------------------------------
    def new_admission(self):
        print("\nAdd Student Details:")

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        clas = int(input("Enter student class (1-12): "))
        mobile = input("Enter guardian mobile number: ")

        if 5 <= age and age <= 18:
            if 1 <= clas and clas <= 12:
                if len(mobile) == 10 and mobile.isdigit():
                    self.admission[self.next_student_id] = {
                        "name": name,
                        "age": age,
                        "class": clas,
                        "mobile": mobile
                    }
                    print("Student successfully admitted!")
                    print("Assigned Student ID:", self.next_student_id)
                    self.next_student_id += 1
                else:
                    print("Mobile number must be exactly 10 digits.")
            else:
                print("Class must be between 1 and 12.")
        else:
            print("Age must be between 5 and 18.")

    # -------------------------------------------------
    def view_student(self):
        sid = int(input("Enter student ID: "))

        if sid in self.admission:
            s = self.admission[sid]
            print("\nStudent Details")
            print("ID:", sid)
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Class:", s["class"])
            print("Guardian Mobile:", s["mobile"])
        else:
            print("Student not found.")

    # -------------------------------------------------
    def update_student(self):
        sid = int(input("Enter student ID to update: "))

        if sid in self.admission:
            student = self.admission[sid]
            print("1. Update Mobile Number")
            print("2. Update Class")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    new_mobile = input("Enter new mobile number: ")
                    if len(new_mobile) == 10 and new_mobile.isdigit():
                        student["mobile"] = new_mobile
                        print("Mobile number updated successfully.")
                    else:
                        print("Invalid mobile number! Must be 10 digits.")
                case 2:
                    new_class = int(input("Enter new class (1-12): "))
                    if 1 <= new_class <= 12:
                        student["class"] = new_class
                        print("Class updated successfully.")
                    else:
                        print("Invalid class! Must be between 1-12.")
                case _:
                    print("Invalid update choice.")

        else:
            print("Student ID not found.")

    # -------------------------------------------------
    def remove_student(self):
        sid = int(input("Enter student ID to remove: "))

        if sid in self.admission:
            self.admission.pop(sid)
            print("Student record deleted successfully.")
        else:
            print("Student ID not found.")

    # -------------------------------------------------
    def run(self):
        while True:
            print("\n--- School Management System ---")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")

            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    self.new_admission()
                case 2:
                    self.view_student()
                case 3:
                    self.update_student()
                case 4:
                    self.remove_student()
                case 5:
                    print("Thank you for visiting...")
                    break
                case _:
                    print("Invalid choice! Please try again.")


# -------------------------------------------------

school = SchoolManagement()
school.run()

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

admission={}
student_id = 1 
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
            print("Add the data of student:=======")
            name=input("Enter student name: ")
            age=int(input("Enter student age: "))
            clas=int(input("Enter student clas: "))
            mobile=input("Enter parents contact number: ")
            if age>=5 and age<=18:
                if clas>=1 and clas<=12:
                    if len(mobile) == 10 and mobile.isdigit():
                        admission[student_id]={"name": name,
                                                "age": age,
                                                "class": clas,
                                                "mobile": mobile}
                        print("Student is successfully added")              
                    else:
                        print("mobile number must be in 10 digit")
                else:
                    print("class must be 1 to 12")
            else:
                print("age must be between 5-18")
            student_id+=1
            print("List of students:")          
            for stud_id, info in admission.items():
                print(f"ID: {stud_id}, Name: {info['name']}, Class: {info['class']}")

           
        case 2:
            print("Student Details:======")
            student_id=int(input("enter student id: "))
            if student_id in admission:
                s = admission[student_id]
                print("\nStudent Details")
                print("ID:", student_id)
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("class:", s["class"])
                print("Guardian Mobile:", s["mobile"])
            else:
                print("Student not found.")                 

        case 3:
            print("Update Details:===============")            
            student_id = int(input("Enter student ID to update: "))

            if student_id in admission:
                student = admission[student_id]

                print("What do you want to update?")
                print("1. Mobile Number")
                print("2. Class")
                choice_update = int(input("Enter your choice: "))

                if choice_update == 1:
                    new_mobile = input("Enter new mobile number: ")
                    if len(new_mobile) == 10 and new_mobile.isdigit():
                        student["mobile"] = new_mobile
                        print("Mobile number updated successfully.")
                    else:
                        print("Invalid mobile number! Must be 10 digits.")

                elif choice_update == 2:
                    new_class = int(input("Enter new class (1-12): "))
                    if 1 <= new_class <= 12:
                        student["class"] = new_class
                        print("Class updated successfully.")
                    else:
                        print("Invalid class! Must be between 1-12.")

                else:
                    print("Invalid choice.")

            else:
                print("Student ID not found.")

        case 4:
            print("Remove Student:=================")
            student_id=int(input("enter student id: "))
            if student_id in admission:
                 admission.pop(student_id)
            print("delete successfully")

        case 5:
            print("Thank you for visting.....I hope your work has done")
            break
        
        case _:
            print("Invalid choice")
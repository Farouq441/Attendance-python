def add_student(name):
  # Add a student to the attendance file
  with open("attendance.txt", "a") as file:
    file.write(name + "\n")

def mark_attendance(name, status):
  # Mark a student's attendance in the file
  with open("attendance.txt", "r") as file:
    lines = file.readlines()
  with open("attendance.txt", "w") as file:
    for line in lines:
      if line.strip() == name:
        file.write(line.strip() + "," + status + "\n")
      else:
        file.write(line)

def view_attendance(name):
  # View a student's attendance from the file
  with open("attendance.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
      if line.strip().startswith(name):
        attendance = line.strip().split(",")[1:]
        print(attendance)

def main():
  while True:
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
      name = input("Enter student name: ")
      add_student(name)
    elif choice == "2":
      name = input("Enter student name: ")
      status = input("Enter attendance status (P/A): ")
      mark_attendance(name, status)
    elif choice == "3":
      name = input("Enter student name: ")
      view_attendance(name)
    elif choice == "4":
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()

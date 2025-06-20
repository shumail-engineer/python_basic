from datetime import date

total_strength = int(input("Total strength of this class? "))

present_students = []

while True:
    name = input("Write name of student if there is no more plz type 'done': ").strip()
    if name.lower() == "done":
        break
    if name != "":
        present_students.append(name)

present_count = len(present_students)
absent_count = total_strength - present_count

filename = "attendance.txt"
with open(filename, "w") as file:
    file.write("Attendance Record\n")
    file.write(f"Date: {date.today()}\n")
    file.write("--------------------------\n")
    for name in present_students:
        file.write(f"{name} - Present\n")
    file.write("--------------------------\n")
    file.write(f"Total Students   : {total_strength}\n")
    file.write(f"Present Students : {present_count}\n")
    file.write(f"Absent Students  : {absent_count}\n")

print("\n Attendance file Done!")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())
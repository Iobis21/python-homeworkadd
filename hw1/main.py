from data import students, new_student
from functions import write_file, add_student, show_students, average_marks, update_mark

# csv ფაილის შექმნა
write_file(students)

print("All students:")
show_students()

student_id = int(input("\nEnter student id: "))
show_students(student_id)

print("\nAverage marks:")
average_marks()

print("\nUpdate mark")
student_id = int(input("Enter student id: "))
subject = input("Enter subject: ")
mark = int(input("Enter new mark: "))
update_mark(student_id, subject, mark)

# 5. ახალი სტუდენტის დამატება
print()
add_student(new_student)
show_students()

import csv

FILE_NAME = "students.csv"
FIELDS = ["id", "name", "age", "grade", "subject_name", "mark"]


# ფაილიდან ყველა სტუდენტის წაკითხვა
def read_file():
    students = []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["age"] = int(row["age"])
            row["mark"] = int(row["mark"])
            students.append(row)
    return students


# სტუდენტების ჩაწერა ფაილში (id-ის მიხედვით დალაგებული)
def write_file(students):
    students.sort(key=lambda student: student["id"])
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


# 1. სტუდენტის დამატება
def add_student(new_student):
    students = read_file()
    for student in students:
        if student["id"] == new_student["id"]:
            print("Student with this id already exists")
            return
    students.append(new_student)
    write_file(students)
    print("Student added:", new_student["name"])


# 2. ყველა ან ერთი სტუდენტის ნახვა
def show_students(student_id=None):
    students = read_file()
    if student_id is None:
        for student in students:
            print(student)
    else:
        for student in students:
            if student["id"] == student_id:
                print(student)
                return
        print("Student not found")


# 3. საშუალო ქულა საგნების მიხედვით
def average_marks():
    marks = {}
    for student in read_file():
        subject = student["subject_name"]
        if subject not in marks:
            marks[subject] = []
        marks[subject].append(student["mark"])

    for subject in marks:
        average = sum(marks[subject]) / len(marks[subject])
        print(subject, ":", round(average, 2))


# 4. ქულის შეცვლა
def update_mark(student_id, subject_name, new_mark):
    students = read_file()
    for student in students:
        if student["id"] == student_id and student["subject_name"] == subject_name:
            student["mark"] = new_mark
            write_file(students)
            print("Mark updated")
            return
    print("Student not found")

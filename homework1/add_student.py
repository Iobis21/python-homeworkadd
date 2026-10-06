from storage import load_students, save_students


# 1. სტუდენტის დამატება და id-ით დასორტირება
def add_student(student):
    students = load_students()
    if any(s["id"] == student["id"] for s in students):
        print(f"სტუდენტი id={student['id']} უკვე არსებობს")
        return False
    students.append(student)
    save_students(students)  # save_students ასორტირებს id-ის მიხედვით
    print(f"სტუდენტი {student['name']} დაემატა")
    return True

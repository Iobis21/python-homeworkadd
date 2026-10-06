from storage import load_students, save_students


# 4. სტუდენტის ქულის განახლება (id, საგანი, ახალი ქულა)
def update_mark(student_id, subject_name, new_mark):
    students = load_students()
    for s in students:
        if s["id"] == student_id and s["subject_name"] == subject_name:
            s["mark"] = new_mark
            save_students(students)
            print(f"id={student_id}, {subject_name}: ქულა განახლდა -> {new_mark}")
            return True
    print(f"სტუდენტი id={student_id} საგნით {subject_name} ვერ მოიძებნა")
    return False

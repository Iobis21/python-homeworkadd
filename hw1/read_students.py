from storage import load_students


# 2. ყველა ან კონკრეტული სტუდენტის წაკითხვა
def read_students(student_id=None):
    students = load_students()
    if student_id is None:
        return students
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def print_students(student_id=None):
    result = read_students(student_id)
    if result is None:
        print(f"სტუდენტი id={student_id} ვერ მოიძებნა")
    elif isinstance(result, list):
        for s in result:
            print(s)
    else:
        print(result)

import os
import sys

from config import CSV_FILE
from data import students, new_student
from storage import save_students
from add_student import add_student
from read_students import print_students
from average import average_by_subject
from update_mark import update_mark


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    # CSV ფაილის შექმნა საწყისი მონაცემებით
    if not os.path.exists(CSV_FILE):
        save_students(students)

    print("--- ყველა სტუდენტი ---")
    print_students()

    print("\n--- სტუდენტი id=11 ---")
    print_students(11)

    print("\n--- საშუალო ქულა საგნების მიხედვით ---")
    for subject, avg in average_by_subject().items():
        print(f"{subject}: {avg}")

    print("\n--- ქულის განახლება ---")
    student_id = int(input("სტუდენტის id: "))
    subject = input("საგანი: ")
    mark = int(input("ახალი ქულა: "))
    update_mark(student_id, subject, mark)

    print("\n--- ახალი სტუდენტის დამატება ---")
    add_student(new_student)
    print_students()


if __name__ == "__main__":
    main()

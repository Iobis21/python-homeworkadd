import csv
import os

from config import CSV_FILE, FIELDNAMES


def _convert(row):
    row["id"] = int(row["id"])
    row["age"] = int(row["age"])
    row["mark"] = int(row["mark"])
    return row


def load_students():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:
        return [_convert(row) for row in csv.DictReader(f)]


def save_students(students):
    students = sorted(students, key=lambda s: s["id"])
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

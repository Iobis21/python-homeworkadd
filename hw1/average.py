from storage import load_students


# 3. საშუალო ქულა საგნების მიხედვით
def average_by_subject():
    totals = {}
    for s in load_students():
        totals.setdefault(s["subject_name"], []).append(s["mark"])
    return {subject: round(sum(m) / len(m), 2) for subject, m in totals.items()}

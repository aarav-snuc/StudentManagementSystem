attendance_records = {}


def mark_attendance(roll, status):
    attendance_records.setdefault(roll, []).append(status)
    print("Attendance marked for", roll, ":", status)


def attendance_percentage(roll):
    records = attendance_records.get(roll, [])
    if not records:
        return 0
    present = records.count("P")
    return (present / len(records)) * 100

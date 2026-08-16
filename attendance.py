def attendance_percentage(roll):
    records = attendance_records.get(roll, [])
    if len(records) == 0:
        print("No attendance records found for", roll)
        return 0.0
    present = records.count("P")
    return round((present / len(records)) * 100, 2)

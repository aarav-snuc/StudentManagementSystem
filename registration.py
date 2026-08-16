def register_student(roll, name, course):
    print("Registered", name, "roll", roll, "for", course)
    return {"roll": roll, "name": name, "course": course}


students = {}

def create_student(name, age, grades):
    students[name] = {"age": age, "grades": grades}

def read_student(name):
    return students.get(name, "Student not found.")

def update_student(name, age=None, grades=None):
    if name in students:
        if age:
            students[name]["age"] = age
        if grades:
            students[name]["grades"] = grades
    else:
        return "Student not found."

def delete_student(name):
    return students.pop(name, "Student not found.")

# Example
create_student("Alice", 20, [85, 90, 92])
print(read_student("Alice"))
update_student("Alice", grades=[88, 91])
print(read_student("Alice"))
delete_student("Alice")
print(read_student("Alice"))

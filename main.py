student_data= {
    "id1": {"name": "John Doe", "age": 20, "major": "Computer Science"},
    "id2": {"name": "Jane Smith", "age": 22, "major": "Mathematics"},
    "id3": {"name": "Alice Johnson", "age": 21, "major": "Physics"},
    "id4": {"name": "Bob Brown", "age": 23, "major": "Chemistry"},
}

result = {}
seen_key = []

for student_id,details in student_data.items():
    unique_key = (details["name"], details["age"], details["major"])
    if unique_key not in seen_key:
        seen_key.append(unique_key)
        result[student_id]=details

for k,v in result.items():
    print(k,":",v)
students = [
    {
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]
print(students[0])
for i in range(0, 1):
    students[i]["sum"] = students[i]["kor"] + students[i]["eng"] + students[i]["math"]
    students[i]["average"] = students[i]["sum"] / 3

print(students)

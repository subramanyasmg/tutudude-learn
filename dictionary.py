studentList = [
    {
        'name': 'alice',
        'marks': 85
    },{
        'name': 'bob',
        'marks': 25
    },{
        'name': 'charlie',
        'marks': 60
    }]

username = input("Enter the student's name: ")
found = False
for student in studentList:
    if student['name'].lower() == username.lower():
        found = True
        print(f"{student['name'].capitalize()}'s marks: {student['marks']}")

if not found:
    print(f"{username.capitalize()}'s not found")

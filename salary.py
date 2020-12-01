salary_people = [
    {"id": int("11"), "salary": int("15000")},
    {"id": int("12"), "salary": int("16000")}
]


def calculate_salary():
    for i in salary_people:
        print(i['salary'])


calculate_salary()

employees = [
    {"name": "Oleg", "id": "11"},
    {"name": "Inga", "id": "12"}
]


def get_employee():
    for sal in employees:
        print(sal['name'], sal['id'])


get_employee()



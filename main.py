from application.salary import calculate_salary
from application.db.people import get_employees
from application.image_printing import print_python_logo
from datetime import date


if __name__ == '__main__':
    print(f"Дата: {date.today().strftime('%d.%m.%Y')}")
    print(calculate_salary())
    print(get_employees())
    print()
    print()
    print()
    print_python_logo()
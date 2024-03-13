
import json
from faker import Faker

fake = Faker()

def generate_employee_details(number_of_records_to_generate):
    """using faker to create list of fake employee data"""
    employee_data = []
    business_unit = ["Finance", "HR", "Marketing", "IT", "Operations"]
    for _ in range(number_of_records_to_generate):
        emp_id = fake.uuid4()[:6]
        emp_name = fake.name()
        emp_email = fake.email()
        business_unit = fake.random.choice(business_unit)
        salary = fake.random_number(digits=5)

        employee_data.append({
            "EMP ID": emp_id,
            "EMP NAME": emp_name,
            "EMP EMAIL": emp_email,
            "Business Unit": business_unit,
            "Salary": salary
        })
    return employee_data

def save_employee_data_to_json(file_name, data):
    """writing data into json file"""
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

number_of_records = fake.random.randint(50,100)
employee_details = generate_employee_details(number_of_records)

FILENAME = "Employee_details.json"
save_employee_data_to_json(FILENAME, employee_details)

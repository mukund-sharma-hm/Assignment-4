"""
This module contains a class called Employee which represents an employee.
It also has methods to set default values for these attributes using the Faker library.
The class has a method convert_to_json which converts the employee object to a json object.
The class also has a static method convert_to_json_write_to_file
which takes an employee object or a list of employee objects and
writes the json representation of the object(s) to a file.
"""

import json
from faker import Faker


jobs = ["Finance", "HR", "Marketing", "IT", "Operations"]
FILENAME = 'Employee_details.json'

with open(FILENAME, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

fake = Faker()


class Employee():
    """This is Class for Employees 

    Args:
        None
    """

    def __init__(self,
                 emp_id=None,
                 emp_name=None,
                 emp_email=None,
                 business_unit=None,
                 salary=None):
        """The constructor for Employee class

        Args:
            emp_id (str, optional): Employee id. Defaults to None.
            emp_name (str, optional): Employee Name. Defaults to None.
            emp_email (str, optional): Employee email. Defaults to None.
            business_unit (str, optional): Employee business unit. Defaults to None.
            salary (int, optional): Employee salary. Defaults to None.
        """
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.business_unit = business_unit
        self.salary = salary


    # setter methods to set values
    def set_emp_id(self, emp_id):
        """Sets the employee's id to provided value.

        Args:
            emp_id (str): the new id to set for the employee

        Returns:
            None
        """
        self.emp_id = emp_id

    def set_emp_name(self, emp_name):
        """Sets the employee's name to the provided value.

        Args:
            emp_name (str): the new name to set for the employee.

        Return:
            None
        """
        self.emp_name = emp_name

    def set_emp_email(self, emp_email):
        """Sets the employee's email to the provided value

        Args:
            emp_email (str): the new emale to set for the employee

        Return:
            None
        """
        self.emp_email = emp_email

    def set_business_unit(self, business_unit):
        """Sets the employee business unit to the provided value

        Args:
            business_unit (str): the new business unit to set for the employee

        Return:
            None
        """
        self.business_unit = business_unit

    def set_salary(self, salary):
        """Sets the employee salary to the provided value

        Args:
            salary (int): the new salary to set for the employee

        Return:
            None
        """
        self.salary = salary

    #setter method to set values using faker
    def set_default_emp_id(self):
        """_Sets a default employee id using faker library
        """
        self.emp_id = fake.uuid4()[:5]

    def set_default_emp_name(self):
        """Sets a default employee name using the Faker library.

        Args:
            None

        Returns:
            None
        """
        self.emp_name = fake.name()

    def set_default_emp_email(self):
        """Sets a default employee email using the Faker library.

        Args:
            None

        Returns:
            None
        """
        self.emp_email = fake.email()

    def set_default_business_unit(self):
        """Sets a default employee business unit using the Faker library.

        Args:
            None

        Returns:
            None
        """
        self.business_unit = fake.random.choice(jobs)

    def set_default_salary(self):
        """Sets a default employee salary using the Faker library.

        Args:
            None

        Returns:
            None
        """
        self.salary = fake.random_number(digits=5)

    #getter methods to get the values

    def get_emp_id(self):
        """Gets the employee ID for this Employee object.

        Args:
            None

        Returns:
            emp_id - str: The employee's ID number.
        """
        return self.emp_id

    def get_emp_name(self):
        """Gets the employee name for this Employee object.

        Args:
            None

        Returns:
            emp_name - str: The employee's ID number.
        """
        return self.emp_name

    def get_emp_email(self):
        """Gets the employee ID for this Employee object.

        Args:
            None

        Returns:
            emp_email - str: The employee's email address.
        """
        return self.emp_email

    def get_business_unit(self):
        """Gets the employee ID for this Employee object.

        Args:
            None

        Returns:
            emp_business_unit - str: The employee's business unit.
        """
        return self.business_unit

    def get_salary(self):
        """Gets the employee salary for this Employee object.

        Args:
            None

        Returns:
            emp_salary - int: The employee's salary.
        """
        return self.salary


    def convert_to_json(self):
        """Converts the Employee object into json-compatible dictionary format.

        Args:
            None

        Returns:
            {} - dict: A dictionary containing employee ID, name, email, business unit, and salary.
        """
        return {
            "EMP ID": self.emp_id,
            "EMP NAME": self.emp_name,
            "EMP EMAIL": self.emp_email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }
    @staticmethod
    def convert_to_json_write_to_file(emp_data, file_name):
        """Static method that converts employee data to JSON format and writes it to a file.

        Args:
            emp_data : Employee object or list of employee objects to  be converted
            file_name (str):  File name in which to write the JSON data.

        Raises:
            ValueError:  If emp_data is not an Employee object  or a list of Employee objects.

        Returns:
            None
        """

        if isinstance(emp_data, Employee):
            converted_data = emp_data.convert_to_json()

        elif isinstance(emp_data, list) and all(isinstance(emp, Employee) for emp in emp_data):
            converted_data = [emp.convert_to_json() for emp in emp_data]

        else:
            raise ValueError("unexpected data type or structure")

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(converted_data, file, indent=4)


employees = []

for records in data:
    employee_id = records["EMP ID"]
    employee_name = records["EMP NAME"]
    employee_email = records["EMP EMAIL"]
    emp_business_unit = records["Business Unit"]
    emp_salary = records["Salary"]

    employee = Employee(employee_id, employee_name, employee_email, emp_business_unit, emp_salary)
    employees.append(employee)


employee = Employee()

employee.set_emp_id(12345)
employee.set_emp_name("Mukund Sharma")
employee.set_emp_email("mukund@example.com")
employee.set_business_unit("Finance")
employee.set_salary(80000)

employee_new = Employee()

employee_new.set_default_emp_id()
employee_new.set_default_emp_name()
employee_new.set_default_emp_email()
employee_new.set_default_business_unit()
employee_new.set_default_salary()


Employee.convert_to_json_write_to_file([employee, employee_new], "list_employee_to.json")

print(vars(employee))

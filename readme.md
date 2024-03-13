# Employee Module Readme

This readme provides information about the Employee module, which contains a class representing an employee with various attributes and methods.

## Employee Class

The Employee class in this module represents an employee and includes the following methods:

### Initialization Method

`__init__(self, emp_id, emp_name, emp_email, business_unit, salary)`: Initializes the employee object with the provided attributes.

### Setter Methods

- `set_emp_id(self, emp_id)`: Sets the employee ID.
- `set_emp_name(self, emp_name)`: Sets the employee name.
- `set_emp_email(self, emp_email)`: Sets the employee email.
- `set_business_unit(self, business_unit)`: Sets the business unit.
- `set_salary(self, salary)`: Sets the salary.

### Default Setter Methods

- `set_default_emp_id(self)`: Sets a default employee ID using Faker.
- `set_default_emp_name(self)`: Sets a default employee name using Faker.
- `set_default_emp_email(self)`: Sets a default employee email using Faker.
- `set_default_business_unit(self)`: Sets a default business unit using Faker.
- `set_default_salary(self)`: Sets a default salary using Faker.

### Getter Methods

- `get_emp_id(self)`: Retrieves the employee ID.
- `get_emp_name(self)`: Retrieves the employee name.
- `get_emp_email(self)`: Retrieves the employee email.
- `get_business_unit(self)`: Retrieves the business unit.
- `get_salary(self)`: Retrieves the salary.

### JSON Conversion Method

- `convert_to_json(self)`: Converts the employee object to a JSON object.

### Static Method for JSON Conversion and File Writing

- `convert_to_json_write_to_file(emp_data, file_name)`: Converts one or more employee objects to JSON and writes them to a file.

## Usage

To use this module effectively:

1. Create an instance of the Employee class by providing necessary details or use default values.
2. Utilize setter methods to update attributes as needed.
3. Access getter methods to retrieve specific information about an employee.
4. Convert an employee object to JSON using the `convert_to_json` method.
5. Write one or more employees to a JSON file using the static method `convert_to_json_write_to_file`.


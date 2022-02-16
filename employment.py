class Employee:
  def __init__(self, name, category, hourly_rate, sick_days, leave_days):
    self.name = name
    self.category = category
    self.hourly_rate = hourly_rate
    self.sick_days = sick_days
    self.leave_days = leave_days
    employee_list.append(self)

def calculate_pay(self, hours_worked):
  gross_pay = hours_worked * self.hourly_rate
  return gross_pay

def do_sick_leave(self, days):
  if days > 0 and days < self.sick_days:
    self.sick_days -= days
    return self.sick_days

def do_annual_leave(self, days):
  if days > 0 and days < self.leave_days:
    self.leave_days -= days
    return self.leave_days

 # Create list to store employee objects
employee_list = []

# Open file with employee data
data_file = open("employees.txt", "r")
employees = data_file.readlines()

# Loop through each line, and split values into list to create employee
for employee in employees:
  employee_data = employee.strip().split(",")
  Employee(*employee_data)

# Print the first employee's name to check it worked.
print(employee_list[0].name, employee_list[0].hourly_rate)

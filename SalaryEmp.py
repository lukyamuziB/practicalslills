from Employee import Employee
class Salaried_Employee(Employee):
	"""Class for an Employee that earns a weeklky salary"""
	def __init__(self,first_name,last_name,social_security_number,weekly_salary):
		

		if weekly_salary < 0.0:
			raise ValueError("Sorry, weekly salary cant be less than 0")
		self._first_name = first_name
		self._last_name = last_name
		self._social_security_number = social_security_number
		self._weekly_salary = weekly_salary

	def set_salary(self, ammount):
		if ammount < 0.0:
			raise ValueError("Sorry, weekly salary cant be less than 0")
	def get_salary(self):
		return self._weekly_salary

	def earnings(self):
		return self._weekly_salary*4
	def report(self):
		a = Salaried_Employee.earnings(self)
		print("First Name: %s\nLast Name: %s\nSocial Number: %s\nWeekly Salary: %.3f\nEarns: %.3f\n"%(self._first_name,self._last_name,self._social_security_number,self._weekly_salary,a))


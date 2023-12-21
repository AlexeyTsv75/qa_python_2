class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.salary_week = None
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days)*8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f'{name}@email.com'
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        self.salary_week = self.hours * self.hourly_payment
        return self.salary_week

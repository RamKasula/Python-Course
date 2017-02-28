class  Employee:

    num_of_employee =   0

    def __init__(self,firstName,lastName,cell,city,state):
        self.firstName  =   firstName
        self.lastName   =   lastName
        self.cell       =   cell
        self.city       =   city
        self.state      =   state

        Employee.num_of_employee    +=  1

    def first_last(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def greeting(self):
        print('Hello my name is',first_last(self))

    @classmethod
    def salary(cls,amount):
        cls.amount      =   amount

    @classmethod
    def bonus(cls, income):
        cls.income =    income

Employee.salary(5000)
Employee.bonus(1000)


employee1 = Employee('Ram','Yadav','270-259-3007','Plano','TX')
employee2 = Employee('Alex','Gib','295-859-9007','Dallas','TX')
employee3 = Employee('Kyle','Rob','159-259-7595','Murray','KY')

print(Employee.num_of_employee)
employee1 = Employee('Ram','Yadav','270-259-3007','Plano','TX')
print(Employee.num_of_employee)
employee2 = Employee('Alex','Gib','295-859-9007','Dallas','TX')
print(Employee.num_of_employee)
employee3 = Employee('Kyle','Rob','159-259-7595','Murray','KY')

print(employee1)
print(employee2)
print(employee3)

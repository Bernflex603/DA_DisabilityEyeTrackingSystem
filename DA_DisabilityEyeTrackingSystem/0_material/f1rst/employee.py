
class Employee():
    def __init__(self, surname: str, givenname: str, salary: float):
        self.surname = surname
        self.givenname = givenname
        self.salary = salary
    
    @staticmethod
    def headers():
        return ['Vorname', 'Nachname', 'Gehalt']
    
    def __repr__(self):
        return f'{self.givenname}, {self.surname}: salary {self.salary}€'



class Executive(Employee):
    def __init__(self, surname: str, givenname: str, salary: float, car: str):
        super().__init__(surname, givenname, salary)
        self.car = car
    
    def __repr__(self):
        return super().__repr__() + f' car: {self.car}'




def main():
    a = Employee('Huber', 'Franz', 10000)
    b = Executive('Berger', 'Herbert', 20000, 'BMW')
    print(a)
    print(b)
    print(Employee.headers())
    
    employees = []
    employees.append(a)
    employees.append(b)
    
    for e in employees:
        print(e)


if __name__ == '__main__':
    main()
    
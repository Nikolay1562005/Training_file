class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.on_work = True
        self.is_good_employee = is_good_employee

    def get_info(self):
        print(f'У {self.name} зп в год составляет {self.salary * 12} руб')


def get_info_employees(employees_list):
    for employee in employees_list:
        employee.get_info()

employees_list = [
    Employee('Петя', 100_000, False, True),
    Employee('Ваня', 10_000, False, True),
    Employee('Игорь', 50_000, False, True),
    Employee('Игорь', 50_000, False, False),
    Employee('Игорь', 50_000, False, True)
]

while True:
    print('-'*80)
    print('1 - получить информацию о всех сотрудниках')
    print('2 - получить информацию об одном сотруднике')
    print('3 - найти неэффективных сотрудников')
    print('4 - выход')
    choice = input('Введите номер команды: ')
    if choice == '1':
        get_info_employees(employees_list)
    elif choice == '2':
        name = input('Введите имя сотрудника: ')
        for employee in employees_list:
            if employee.name == name:
                employee.get_info()
                break
    elif choice == '3':
        for id, employee in  enumerate(employees_list):
            if employee.is_good_employee == False:
                employee.get_info()
                choice_about_dismissal = (input('Вы хотите удалить этого сотрудника?(да\нет) \n'))
                if choice_about_dismissal == 'да':
                    employees_list.pop(id)
    else:
        print('Пока!')
        break
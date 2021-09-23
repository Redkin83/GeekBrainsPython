'''Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего 
 разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на
 экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников 
 из элементов списка, как привести их к корректному виду. Можно ли при этом 
 не создавать новый список?'''
 
employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 
             'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for employee in employees:
    print('Привет,' + employee.split()[-1].title() + '!')

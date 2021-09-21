''' Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится 
нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 
6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только 
арифметические операции!К каждому элементу списка добавить 17 и заново 
вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело 
на 7.
* Решить задачу под пунктом b, не создавая новый список.'''

number = []
for i in range(1, 1001):
    if i%2!=0:
        number.append(i*i*i)
res=0
res1=0
for n in number:
    s=0
    while n%10!=0:
        s+=n%10
        n=n//10
    if s%7 == 0:
        res += n       
print(res)
number2 = []
for n in number:
    number2.append(n+17)
    s=0
    n+=17
    while n%10!=0:
        s+=n%10
        n=n//10
    if s%7 == 0:
        res1 += n  
print(res1)
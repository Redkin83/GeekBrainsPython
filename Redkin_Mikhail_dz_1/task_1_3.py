'''Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту 
фразу на экран отдельной  строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов

Задачи со * предназначены для продвинутых учеников, которым мало сделать 
обычное задание. Пробуйте их решать, если уверены в своих силах.'''

for i in range(101):
    if i%10 > 4 or i%10 ==0 or i//10==1:
        print(str(i)+' процентов')
    elif i%10 > 1:
        print(str(i)+' процента')
    else:
        print(str(i)+' процент')
        
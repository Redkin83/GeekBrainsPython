"""
 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек;
 до часа: <m> мин <s> сек; до суток:  <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
"""
durations = [53, 153, 4153, 400153]
Time_duration_desc = ['дн', 'час', 'мин', 'сек']
for duration in durations:
    Time_duration  = []
    d = duration // 86400
    Time_duration.append(d)
    h = (duration - d * 86400) // 3600
    Time_duration.append(h)
    m = (duration - h * 3600 - d * 86400) // 60
    Time_duration.append(m)
    s = duration - m * 60 - h * 3600 - d * 86400
    Time_duration.append(s)

    res = ''
    for index,td in enumerate(Time_duration):
        if td!=0:
            res += str(td) + ' ' + Time_duration_desc[index] + ' '
        
    print(res)
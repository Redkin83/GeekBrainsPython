''' * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, 
in place). Эта задача намного серьёзнее, чем может сначала показаться.'''

'''Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 
 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не 
трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, 
являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 
'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете 
вернуться к его реализации позже. Главное: дополнить числа до двух 
разрядов нулём!'''

words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 
 'градусов']

for word in words:
    word_index = words.index(word)
    words.remove(word)
    if word[0] in ('+', '-'):
        word='"' + word.zfill(3) + '"' 
    if (word.isdigit()):
        word='"' + word.zfill(2) + '"'
    words.insert(word_index, word)
print(' '.join(words))
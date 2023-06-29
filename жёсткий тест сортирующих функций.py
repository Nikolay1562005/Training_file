
import random
import time

class RunningCodeJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'Время выполнения: {t}')
        return True

'''
print('Генератор списка')
with RunningCodeJudge():
    f = open('tx.txt', 'w')
    f.seek(0)
    for i in range(1_000_000):
        f.write(str(random.randint(-100, 1_000_000))+'\n')
    f.close()'''


test_lst = [int(i) for i in open('tx.txt')]
print(len(test_lst))

#---1---
print(str('1'.center(20, '-')))
print('Встроенная функция max()')
with RunningCodeJudge():
    print("Наибольшее число:", max(test_lst))

#---2---
print(str('2'.center(20, '-')))
print('Метод грубой силы (перебора)')
with RunningCodeJudge():
    def large(arr):
        max_ = arr[0]
        for ele in arr:
            if ele > max_:
                max_ = ele
        return max_

    print("Наибольшее число:", large(test_lst))

#---3---
print(str('3'.center(20, '-')))
print('Функция reduce()')
with RunningCodeJudge():
    from functools import reduce

    print("Наибольшее число:", reduce(lambda x, y: x if x > y else y, test_lst))

#---4---
print(str('4'.center(20, '-')))
print('Алгоритм Heap Queue (очередь с приоритетом)')
with RunningCodeJudge():
    import heapq
    print("Наибольшее число:", heapq.nlargest(1, test_lst))

#---5---
print(str('5'.center(20, '-')))
print('Функция sort()')
with RunningCodeJudge():
    t = test_lst.sort()
    print("Наибольшее число:", t)


#---6---
print(str('6'.center(20, '-')))
print('Функция sorted()')
with RunningCodeJudge():
    print("Наибольшее число:", sorted(test_lst)[-1])

#---7---
print(str('7'.center(20, '-')))
print('Метод хвостовой рекурсии')
with RunningCodeJudge():
    def find_max(arr, max):
        if max == 0:
            max = arr.pop()
        current = arr.pop()
        if current > max:
            max = current
        if arr:
            return find_max(arr, max)
        return max

    print("Наибольшее число: ", find_max(test_list, 0))
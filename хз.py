from time import*
from random import randint
#with open('tx.txt') as f:
#    print(f.readline())
'''
class RunningCodeJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time() - self.start
        print(f'{exc_tb}\n{exc_val}\n{exc_tb}')
        print(f'Время выполнения: {t}')
        return True

with RunningCodeJudge():
    lst = [abs(i) for i in range(1_000_000)]
    lst - 1

lst = [1, 2 , 3]
my_iterator = iter(lst)

for i in my_iterator:
    print(i)'''

class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit == self.__reload
        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration  # принудительно вызывает ошибку
        self.limit -= 1
        return randint(1, 100)

rand_iter = RandomIter(5)
for i in rand_iter:
    print(i)

rand_iter = RandomIter(9)
for i in rand_iter:
    print(i)
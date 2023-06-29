import contextlib

lst = [3, 7, 9, 8]

def lazy_func(lst):
    yield from lst

for i in lazy_func(lst):
    print(i)


with open('tx.txt', 'w') as f:
    f.write('hiii')

@contextlib.contextmanager
def str_reverse(my_str):
    yield my_str[::-1]

with str_reverse('goood') as s:
    print(f'Выполняем действия: {s}')

@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield  True
    except exc:
        print('eror!!!')

with  exc_handler(IndexError):
    s = [9, 3, 8]
    print(s[9])

def func(*args, **kwargs):
    print(f'арги: {args}\nКварги: {kwargs}')

func(4, 65, 353, 3536, 488, a=7)
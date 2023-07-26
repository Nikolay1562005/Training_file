class MyFile:
    def __init__(self, name, mode, encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyFile('myfile.txt', 'r') as file:
    print(file.read())


class InfiniteIterator:
    def __init__(self):
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        self.start -= 1

for i in InfiniteIterator():
    print(i)
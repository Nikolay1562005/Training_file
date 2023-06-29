def palindrome(word):
    return word == word[::-1]


if __name__ == "__main__":
    while True:
        word = input("Введите слово: ")
        if word.count(" ") == 0:
            print(f'Это слово палиндром: {palindrome(word.lower())}')
        else:
            print("Нужно вводить слово, а не выражение!")
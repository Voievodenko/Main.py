name = 'text.txt'


def change(file, word1, word2):
    with open(file, 'r', encoding='utf-8') as func:
        text = func.read()

    update = text.replace(word1, word2)

    with open(file, 'w', encoding='utf-8') as rep:
        rep.write(update)


word1 = input("Введіть слово для заміни: ")
word2 = input("Введіть слово, на яке потрібно замінити: ")

change(name, word1, word2)

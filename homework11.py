bad_words = ['ploxoe_clovo', 'matuk']
separators = [".", '!', ',', '...', '?']


def cenzor():
    with open('file.txt', 'r') as file:
        text = file.read()
        for i in bad_words:
            if i in text:
                text = text.replace(i, "***")
        with open('file_new.txt', 'w') as file:
            file.writelines(text)


cenzor()


def ex2():
    with open('file.txt', 'r') as file:
        text = file.read()
        for separator in separators:
            if separator in text:
                text = text.replace(separator, "")
        text = text.split()
        res_dct = {text[word]: len(text) for word in range(0, len(text), 1)}
        return res_dct


print(ex2())

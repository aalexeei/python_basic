import json
import csv
import os


def read_file(files_enter):
    """
    :param files_enter:
    :return: text_read
    """
    with open(files_enter, 'r') as file:
        text_read = file.read()
        return text_read


def create_new_file_txt(text_read, bad_words):
    """
    :param text_read:
    :param bad_words:
    :return:
    """
    with open(f'file_new.txt', 'w') as file:
        for word in bad_words:
            text_read = text_read.replace(word, "***")
        file.writelines(text_read)


def create_file_json(files_enter, text_read, bad_words):
    """
    :param files_enter:
    :param text_read:
    :param bad_words:
    :return:
    """
    dict_with_filename_word_count = {files_enter: {word: text_read.count(word) for word in bad_words}}
    if not os.path.exists('file_new.json'):
        with open("file_new.json", "w") as create_file:
            create_file.write("[]")
    with open('file_new.json', 'r') as file:
        list_with_data = json.load(file)
        list_with_data.append(dict_with_filename_word_count)
    with open('file_new.json', 'w') as file:
        json.dump(list_with_data, file)


def create_file_csv(files_enter, text_read, bad_words):
    """
    :param files_enter:
    :param text_read:
    :param bad_words:
    """
    if not os.path.exists('file_new.csv'):
        with open('file_new.csv', "a") as header:
            writer = csv.writer(header, delimiter=';')
            writer.writerow(('filename', 'word', 'count'))
    with open('file_new.csv', "a") as filename:
        writer = csv.writer(filename, delimiter=';')
        word = [word for word in bad_words]
        words_count = [text_read.count(word) for word in bad_words]
        writer.writerow((files_enter, word[0], words_count[0]))
        for word in range(1, len(bad_words)):
            writer.writerow((' ', bad_words[word], text_read.count(bad_words[word]), ' '))

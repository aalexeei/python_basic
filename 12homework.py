from homework12 import *

files_enter = input("Enter name txt file: ") + ".txt"
bad_words = input("Enter bad words or set default: ").split() or ['matuk1', 'matuk2']
text_read = read_file(files_enter)
create_new_file_txt(text_read, bad_words)
create_file_json(files_enter, text_read, bad_words)
create_file_csv(files_enter, text_read, bad_words)

import os


class WorkWithDir:
    def __init__(self,dir_path,status=False):
        self.dir_path = dir_path
        self.status = status

    def get_list_contents(self):
        '''
        метод класса, который создает атрибут класса в ввиде словаря
        {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
        Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
        {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
        :return:
        '''
        dir_list = []
        file_list = []
        for item in os.listdir(self.dir_path):
            if os.path.isdir(item):
                dir_list.append(item)
            else:
                file_list.append(item)
        self.dict_contents ={"dir":dir_list,"file":file_list}

    def sort(self):
        '''
        метод класса, которая получает булевое значение (True/False).
        Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
        Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
        :return:
        '''
        self.dict_contents['dir'].sort(reverse=self.status)
        self.dict_contents['file'].sort(reverse=self.status)
        # print(self.dict_contents)

    def add_item(self, item):
        '''
        метод класса, которая получает строку, которая может быть
        или именем файла, или именем папки. (В имени файла должна быть точка).
        В зависимости от того, что функция получила (имя файла или имя папки) - записать его
        в соответствующий список и вернуть обновленный словарь.
        :param item:
        :return: self.content
        '''
        if '.' in item[1:]:
            self.dict_contents['file'].append(item)
        else:
            self.dict_contents['dir'].append(item)
        return self.dict_contents


dir = WorkWithDir(".")
dir.get_list_contents()
dir.sort()
dir.add_item(".ttt.txt")
dir.add_item("ttt.txt")
print(dir.add_item("ttt"))


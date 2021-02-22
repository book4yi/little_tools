# -*- coding: UTF-8 -*-
import chardet


def check_code(text):
    adchar = chardet.detect(text)
    if adchar['encoding'] == 'gbk' or adchar['encoding'] == 'GBK' or adchar['encoding'] == 'GB2312':
        true_text = text.decode('GB2312', "ignore")
    else:
        true_text = text.decode('utf-8', "ignore")
    return true_text


def read_file_text(file_url):
    f = open(file_url, 'rb')
    file_text = f.read()
    file_text = check_code(file_text)
    return file_text


def get_unique_list():
    global c
    words = read_file_text(r'C:\Users\sws123\Desktop\100.txt')
    key = words.split('\n')
    for i in range(len(key)):
        # if len(key[i].strip()) > 3:
        a.add(key[i])
    b = list(a)
    b.sort()
    c = len(key) - len(a)
    ft = open(r"C:\Users\sws123\Desktop\100.txt", 'w+')
    ft.writelines(b)
    ft.close()


def main():
    get_unique_list()
    print('done')
    print("Repeated Count:", c)
    print("Remaining Count:", len(a))


if __name__ == '__main__':
    global c
    a = set()
    main()

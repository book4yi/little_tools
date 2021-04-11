import pypinyin
from pypinyin import Style, lazy_pinyin

dict_list = []


def generate_rule(name):
    rule_name4 = ''
    pinyin = pypinyin.slug(name, separator='')
    first_letter = pypinyin.slug(name, style=Style.FIRST_LETTER, separator='')
    pinyin_list = lazy_pinyin(name)
    first_letter_list = lazy_pinyin(name, style=Style.FIRST_LETTER)
    # print(pinyin_list)
    # print(first_letter_list)
    # print(pinyin)
    # print(first_letter)
    if len(pinyin_list) == 3:
        rule_name1 = pinyin_list[0] + first_letter_list[1] + first_letter_list[2]
        rule_name2 = first_letter_list[0] + pinyin_list[1] + pinyin_list[2]
        rule_name3 = pinyin_list[1] + pinyin_list[2]
        rule_name4 = pinyin_list[1] + pinyin_list[2] + first_letter_list[0]
        rule_name5 = pinyin_list[1] + pinyin_list[2] + pinyin_list[0]
        rule_name6 = pinyin_list[2] + first_letter_list[0] + first_letter_list[1]
    elif len(pinyin_list) == 2:
        rule_name1 = pinyin_list[0] + first_letter_list[1]
        rule_name2 = first_letter_list[0] + pinyin_list[1]
        rule_name3 = pinyin_list[1] + first_letter_list[0]
    dict_list.append(first_letter)
    dict_list.append(pinyin)
    dict_list.append(rule_name1)
    dict_list.append(rule_name2)
    dict_list.append(rule_name3)
    if rule_name4:
        dict_list.append(rule_name4)
        dict_list.append(rule_name5)
        dict_list.append(rule_name6)
    pinyin_list.clear()
    first_letter_list.clear()


def main():
    with open(r'C:\Users\sws123\Desktop\name.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        generate_rule(line)
    

if __name__ == '__main__':
    main()
    for single in dict_list:
        print(single)

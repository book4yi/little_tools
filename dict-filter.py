# -*- coding:utf-8 -*-
import sys

num_list, letter_list, mix_list, spe_list = set(), set(), set(), set()
len_list = set()
result_list = set()
num_count, letter_count, mix_count, spe_count = 0, 0, 0, 0

spe_char_list = ['!', '?', ',', '.', ':', ';', '\"', '\'', '`', '*', '+', '-', '=', '/', '\\', '|', '_', '$', '@', '#',
                 '%', '&', '~', '^', '(', ')', '<', '>', '[', ']', '{', '}']

with open(r'D:\dictionary\国外弱密码top500.txt', encoding='utf-8') as f:
    lines = {line.strip() for line in f.readlines()}


def get_list():
    global num_count, letter_count, mix_count, spe_count
    for i in lines:
        # 纯数字字典：
        if i.isdigit():
            num_list.add(i)
            num_count += 1
        # 纯字母字典：
        elif i.isalpha():
            letter_list.add(i)
            letter_count += 1
        # 数字和字母的组合字典：
        elif i.isalnum():
            mix_list.add(i)
            mix_count += 1
        # 包含特殊符号的字典：
        else:
            for j in i:
                if j in spe_char_list:
                    spe_list.add(i)
                    spe_count += 1
                    break


# 设置获取字典集合的长度范围
def set_len(target_list, min_len, max_len):
    for i in target_list:
        if min_len <= len(i) <= max_len:
            len_list.add(i)
    return len_list


def main():
    get_list()
    amount = num_count + letter_count + mix_count + spe_count
    if amount != len(lines):
        loss = len(lines) - amount
        print(f'字典词条总数与实际总数不相等,共缺失{loss}条数据')
        sys.exit()
    print(f'num: {num_count}')
    print(f'letter: {letter_count}')
    print(f'mix: {mix_count}')
    print(f'spe: {spe_count}')


if __name__ == "__main__":
    main()
    result_list = set_len(num_list, 6, 10)

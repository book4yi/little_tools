# -*- coding: utf-8 -*-
# @Author: book4yi
# @Date:   2020-08-07 12:20:54
# @Last Modified by:   book4yi
# @Last Modified time: 2020-08-07 20:28:54
import requests
import time
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

requests.packages.urllib3.disable_warnings()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.40',
}


def get_data(xpath, selector1):
    result = selector1.xpath(xpath).extract()
    data = " ".join(result)
    return data


def main():
    with open(r'C:\Users\xxxxx\Desktop\77.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        if line[0:4] != 'http':
            line = 'http://' + line
        if line[-1] != '/':
            line = line + '/'
        url1 = line + 'index.php?s=123'
        try:
            r = requests.get(url=url1, headers=headers, verify=False, timeout=10)
            # print(f'访问{url1}')
            html = r.text
            response = HtmlResponse(html, body=html, encoding='utf-8')
            selector = Selector(response=response)
            data_xpath = f'normalize-space(/html/body/div[2]/p/sup)'
            datas = get_data(data_xpath, selector)
            tp_type = 1
            if not datas:
                data_xpath = f'normalize-space(/html/body/div[3]/span[1])'
                datas = get_data(data_xpath, selector)
                tp_type = 2
            if not datas:
                data_xpath = f'normalize-space(/html/body/div[4]/span[1])'
                datas = get_data(data_xpath, selector)
                tp_type = 3
            if datas:
                print(f'{url1}\tthinkphp版本：\t{datas}\t{tp_type}')
        except:
            pass


if __name__ == '__main__':
    main()

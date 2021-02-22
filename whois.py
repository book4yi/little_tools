import requests
import json
import sys
import time
import xlsxwriter


def submit_data(domain):
    global taskid
    url = 'http://apidata.chinaz.com/BatchAPI/Whois'
    datas = {'key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'domainNames': domain}
    r = requests.post(url, data=datas)
    json_data = json.loads(r.text)
    print(json_data)
    if json_data['Reason'] == '提交成功':
        taskid = json_data['TaskID']
        return taskid
    else:
        sys.exit()

def get_data(taskid):
    id = taskid
    url2 = 'http://apidata.chinaz.com/batchapi/GetApiData'
    if taskid:
        datas2 = {'taskid': taskid}
        r2 = requests.post(url2, data=datas2)
        result = json.loads(r2.text)
        if result['Reason'] == '成功':
            info = result['Result']
            info_dict = {'SubmitCount': info['SubmitCount'], 'SuccessCount': info['SuccessCount']}
            print(info_dict)
            return result['Result']['Data']
        else:
            time.sleep(10)
            return get_data(id)
    
    
if __name__ == "__main__":
    domain = ''
    taskid = ''
    a, b, c, d, e, f, g, data_list, all_data = [], [], [], [], [], [], [], [], []
    workbook = xlsxwriter.Workbook(r'C:\Users\xxxxx\Desktop\whois2.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    headings = ['Host', 'ContactPerson', 'Registrar', 'Email', 'Phone', 'CreationDate', 'ExpirationDate']
    with open(r'C:\Users\xxxxx\Desktop\100.txt', 'r') as fr:
        lines = [line.strip() for line in fr.readlines()]
    for line in lines:
        domain = domain + line + '|'
    domain = domain.rstrip('|')
    taskid = submit_data(domain)
    result = get_data(taskid)
    for i in result:
        print(i['Result'])
        data_list.append(str(i['Result']) + '\n')
        if i['Reason'] == '成功':
            a.append(i['Result']['Host'])
            b.append(i['Result']['ContactPerson'])
            c.append(i['Result']['Registrar'])
            d.append(i['Result']['Email'])
            e.append(i['Result']['Phone'])
            f.append(i['Result']['CreationDate'])
            g.append(i['Result']['ExpirationDate'])
        else:
            a.append(i['Domain'])
            b.append(0)
            c.append(0)
            d.append(0)
            e.append(0)
            f.append(0)
            g.append(0)
    all_data.append(a)
    all_data.append(b)
    all_data.append(c)
    all_data.append(d)
    all_data.append(e)
    all_data.append(f)
    all_data.append(g)
    worksheet.write_row('A1', headings)
    worksheet.write_column('A2', all_data[0])
    worksheet.write_column('B2', all_data[1])
    worksheet.write_column('C2', all_data[2])
    worksheet.write_column('D2', all_data[3])
    worksheet.write_column('E2', all_data[4])
    worksheet.write_column('F2', all_data[5])
    worksheet.write_column('G2', all_data[6])
    workbook.close()

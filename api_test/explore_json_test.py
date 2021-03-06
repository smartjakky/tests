import requests
import json
from urllib.parse import urlencode, unquote, unquote_plus


def get_explore_json(host, port=80, force='true'):
    cookies = {
        "session": ".eJx9z8tuwyAQheF3mbVlLgEb8ypRZQEzxCi0toA0iqK8e4nadff_d6TzhDUWqhvYVm40wJoQLBinI9EigneT5t6gRhTOx2Amc1ITwgChlri2_UpfvRecTzIoF6VHotlov2ivFCehFk7zgjO6IOLb5T24TN10OMDhLrRuqba9PMCeYWvtsIwJPgopRzmPSlnDxYnVkNitUqks95p1-m9acwr0uSPl70T3P_MxwHvi96KE1w-H5kvz.DXaeFg.O68cESiTo16EgSqFPdNc3UHDmBw"
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }

    host = 'http://{}:{}/'.format(host, port)
    path = 'sci/superset/explore_json/table/{}'
    with open('D:\\home\\pivot_viz\\form_data.json', 'r') as f:
        content = f.read()
        form_data = json.loads(content)
        print(form_data['datasource'].split('__')[0])
        url = host + path.format(form_data['datasource'].split('__')[0]) + '?' + urlencode({'form_data': content, 'force': force})
        print(unquote_plus(url))
    res = requests.get(url, headers=headers, cookies=cookies)

    print(res.status_code)
    with open('D:\\home\\pivot_viz\\response.json', 'w', encoding='utf8') as f:
        f.write(res.content.decode())
    return json.loads(res.content.decode()).get('query')


if __name__ == '__main__':
    # sql = get_explore_json('10.122.22.113')
    # sql = get_explore_json('10.122.27.44', 8088)
    # sql = get_explore_json('127.0.0.1', 8088)
    # sql = get_explore_json('10.122.27.44', 8013)
    sql = get_explore_json('10.122.27.44', 8088)
    print(sql)

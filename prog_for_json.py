import json
from collections import Counter
from pprint import pprint
needed_len = 6
news_list = []
long_list = []
result = []
cnt = Counter()
def find_top():
    with open('newsafr.json', encoding= 'utf-8') as file:
        data = json.load(file)
        for news in data['rss']['channel']['items']:
            news_list.append(news['description'])
        for words in news_list:
            words = words.lower().split()
        work_with(words)


def work_with(words):
    for words in news_list:
        words = words.lower().split()
    for len6 in words:
        if len(len6) >= needed_len:
            long_list.append(len6)
    for word in long_list:
        cnt[word] += 1
    for k, v in cnt.items():
        if v != 1:
            result.append(k)
    print(f'Топ поторяющихся слов: {result}')

find_top()










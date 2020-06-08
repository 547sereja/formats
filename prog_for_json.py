

import json


def func_split_news_from_json():
    with open('newsafr.json', encoding='utf-8') as file:
        data = json.load(file)
        for all_news in data['rss']['channel']['items']:
            each_word = all_news['description'].lower().split()

    return each_word


def look_for_most_common_words(each_word):
    needed_len = 6
    more_6_len_list = []
    for needed_words in each_word:
        if len(needed_words) >= needed_len:
            more_6_len_list.append(needed_words)

    more_6_len_list.sort(key=more_6_len_list.count, reverse=True)
    top10 = ' '.join(more_6_len_list[0:10])

    return top10





print(look_for_most_common_words(func_split_news_from_json()))
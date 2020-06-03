import json


def func_split_news_from_json():
    with open('newsafr.json', encoding= 'utf-8') as file:
        data = json.load(file)
        all_text_from_news = []
        for all_news in data['rss']['channel']['items']:
            all_text_from_news.append(all_news['description'])
        for each_word in all_text_from_news:
            each_word = each_word.lower().split()
    return each_word


func_split_news_from_json()


def look_for_most_common_words(each_word):
    needed_len = 6
    more_6_len_list = []
    for needed_words in each_word:
        if len(needed_words) >= needed_len:
            more_6_len_list.append(needed_words)

    more_6_len_list.sort(key=more_6_len_list.count, reverse=True)
    top10 = list(set(more_6_len_list[0:11]))

    return top10


print(look_for_most_common_words(func_split_news_from_json()))



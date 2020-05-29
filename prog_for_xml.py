import xml.etree.ElementTree as ET
from collections import Counter
needed = 6
words_list = []
cnt = Counter()
result = []
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
print(root)
print(root.tag)
print(root.text)
print(root.attrib)
xml_items = root.findall("channel/item")
print(len(xml_items))
print(type(xml_items))
for item in xml_items:
    all_news = item.find("description").text.split()
for word in all_news:
    if len(word) >= needed:
        words_list.append(word)
for word6 in words_list:
    cnt[word6] += 1
    for key, val in cnt.items():
        if val != 1:
            result.append(key)
b = sorted(result, key=result.count, reverse=True)
print(f"Самые повторяемые слова: {set(b)}")



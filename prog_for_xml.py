import prog_for_json


def func_split_news_from_xml():
    import prog_for_json
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")
    for all_news in xml_items:
        each_word = all_news.find("description").text.lower().split()
    return each_word


prog_for_json.look_for_most_common_words(func_split_news_from_xml())













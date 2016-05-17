from html.parser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
parser = MyHTMLParser()
texts = str()
for _ in range(int(input().strip())):
    texts += input()
texts = re.sub(r"\<\!--.*?--\>", "", texts)
parser.feed(texts)
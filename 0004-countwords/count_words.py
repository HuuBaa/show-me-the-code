#任一个英文的纯文本文件，统计其中的单词出现的个数。

# import re

# with open('words.txt','r') as f:
#     text=f.read()

# wordlist=re.findall(r'[A-Za-z]+',text)
# print(wordlist)
# print(wordlist.__len__())



import re
import os
from pprint import pprint

path = os.getcwd() + '/word.txt'


def wordstat(path):
    f = open(path, 'r+')
    wordcount = {}
    
    for t in re.sub('[^0-9a-zA-Z]+', " ", f.read()).split():
        if t not in wordcount:
            wordcount[t] = 1
        else:
            wordcount[t] += 1
    pprint(wordcount)


if __name__ == '__main__':
    wordstat('words.txt')
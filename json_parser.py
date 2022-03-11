
import sys
import json


def parse_json(text_iter):
    total = 0
    # print(list(text_iter)[0])
    for chunk in text_iter:
        # since chunk returns a byte; write a function to check the byte data
        json.loads(chunk)
        for i in chunk:
            if i == 123:
                total += 1
            elif i == 125:
                total -= 1
            # print(total)
            # if total == 0:
            #     print("stop")
            #     return

    # How do I work with unicode??

    # one; I can do sth that allows a complete
    # file to be parsed


    # text_iter = ['byte1', 'byte2', 'byte3']
    list_ = []
    while True:
        # try:
        #     ...
        # except json.decoder.JSONDecodeError:
        #     continue
        sys.exit()
    # for i in text_iter:
    #     print(i)
    #     print("\n")
    #     print(next(text_iter))
    #     sys.exit()
    #     # try:
    #     #     json.loads(i)
    #     # except json.decoder.JSONDecodeError:
    #     #     json.loads(next(i))
    #     # list_.append(json.loads(i))
    return list_


def parse_number():
    pass

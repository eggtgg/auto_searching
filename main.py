import webbrowser
import random


def rand_keyword():
    a = ['pháp', 'anh', 'argentina', 'hà lan', 'mỹ', 'espana', 'moroco', 'viet nam', 'a rap', 'qatar']
    b = ['thua', 'thang', 'hòa', 'tập luyện cùng', 'đá', 'mua', 'chung kết', 'would cup', 've nuoc', 'ngoai giao',
         'phat trien', 'kinh te']
    return random.choice(a) + ' ' + random.choice(b)


def go(keyword):
    link = 'https://www.bing.com/search?q=' + keyword
    webbrowser.open(link)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(40):
        key_word = rand_keyword()
        go(key_word)

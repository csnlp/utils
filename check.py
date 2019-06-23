# -*- coding:utf-8 -*-

import re

def check_contain_letters(str):
    str_l = list(str)
    for c in str_l:
        if c.isalpha():
            return True
    return False

if __name__ == '__main__':
    str1 = '口腔溃疡Ha口腔a'
    str2 = '口腔溃疡h'
    str3 = '口腔溃疡1'
    print check_contain_letters(str1), check_contain_letters(str2),check_contain_letters(str3)

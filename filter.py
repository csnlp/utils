# -*- coding:utf-8 -*-
import re
cop = re.compile("[^\u4e00-\u9fff^、^-]")
line = "1、（您好）北京，天安门hhh、U-8"

filtered_line = cop.sub("", line)

print filtered_line

from collections import Counter
import re
words = re.findall(r'\w+', open('test.txt').read().lower())
count = Counter(words)
srt_dict = sorted(count)
# print(srt_dict)
# srt_dict_value = sorted(count.items(), key = lambda x: x[1])
# for i in srt_dict_value:
    # print(i[0], i[1])
srt_dict_value_desc = sorted(count.items(), key = lambda x: x[1], reverse= True)
for i in srt_dict_value_desc:
    print(i[0], i[1])
import json
import jsonlines
import os
import collections
s = set()
d = collections.defaultdict(int)
with jsonlines.open('autodl-tmp/dataset/agriculture.jsonl') as file:
    for i in file:
        context = i.get('context')
        id = i.get('context_id')
        d[id] += 1
print(d)
res = 0
for i in d :
    res += d[i]
print(res)
        # if id in s:
        #     continue
        # s.add(id)
        # with open(f'autodl-tmp/dataset/agr/{id}.txt','w',encoding='utf-8') as f:
        #     f.write(context)
        # f.close

# files_and_dirs = os.listdir("autodl-tmp/dataset/agr/")     
# for i in files_and_dirs:
#     print(f"autodl-tmp/dataset/agr/{i}")

jsonl_files = ['660ddc2dc66d64e3f60f3da5b6634b9d.jsonl', '129d20a7d780e4daacf221d2ff161857.jsonl', '2948e8343af1d9c6941eeba6067efc0c.jsonl', '75b9cff8f1ef40c875b7c3d52f9f168f.jsonl', '7a758123f10a5721b65661694ababbfc.jsonl', 'f6c2532de0d6c0d7b63f9c3da923fae0.jsonl', '6301eee8863ab1228e1130c776852439.jsonl', 'e12308db46ecd7ab54ec6ede5ad1954a.jsonl', '5c4d27505be8f68d45715fb7060b54ea.jsonl', 'c1bd30eb76e68b45b319f8069b10b91f.jsonl', 'e82bc9884f045d9ca167b6526a116eb3.jsonl', '98a33f1d8593125b320efa556a2c1a39.jsonl']

# 打开一个新的文件用于合并
with open('merged_output.jsonl', 'w') as outfile:
    for file in jsonl_files:
        # 依次读取每个jsonl文件并写入输出文件
        with open(file, 'r') as infile:
            for line in infile:
                outfile.write(line)

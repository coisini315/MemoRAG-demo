# MemoRAG-demo
> 针对`agriculture.jsonl`数据集。

下载Mistral-based记忆模型： https://huggingface.co/TommyChien/memorag-mistral-7b-inst

向量嵌入模型可下可不下，需要注意修改模型位置即可
```bash
pip install memorag
```
## AutoDL使用代理
如需使用代理，可以按照以下步骤执行(针对AutoDL，需要config.yaml文件)。
可以参考： https://zhuanlan.zhihu.com/p/685018159 
```bash
# 新开一个终端并执行以下命令
cd mihomo
./mihomo-linux-amd64-v1.18.1 -d ./
```
```bash
# 在需要代理的终端执行以下命令，然后正常运行其他文件
export https_proxy=http://127.0.0.1:7890/
export http_proxy=http://127.0.0.1:7890/
```
## 切分数据集
使用`split_agr_single.py`文件将jsonl数据集文件中的context提取并分别保存下来。保存路径为`autodl-tmp/dataset/agr`，文件名为数据集中的context_id。
```bash
python autodl-tmp/dataset/split_agr_single.py
```
## conetext记忆化
使用`memory_context.py`文件将对应context记忆至模型KV中并保存到`autodl-tmp/cache/agr`
```bash
python autodl-tmp/memory_context.py
```
每次需要调整处理的context文件名
```python
files_and_dirs = ['660ddc2dc66d64e3f60f3da5b6634b9d.txt', '129d20a7d780e4daacf221d2ff161857.txt', '2948e8343af1d9c6941eeba6067efc0c.txt', '75b9cff8f1ef40c875b7c3d52f9f168f.txt', '7a758123f10a5721b65661694ababbfc.txt', 'f6c2532de0d6c0d7b63f9c3da923fae0.txt', '6301eee8863ab1228e1130c776852439.txt', 'e12308db46ecd7ab54ec6ede5ad1954a.txt', '5c4d27505be8f68d45715fb7060b54ea.txt', 'c1bd30eb76e68b45b319f8069b10b91f.txt', 'e82bc9884f045d9ca167b6526a116eb3.txt', '98a33f1d8593125b320efa556a2c1a39.txt']
filename = files_and_dirs[9] #0 1 2 3 4 5 6 7 8 10 11
```
## （可选）context截断
如果部分context在记忆过程中出现OOM问题，可以使用`cat_bigcontext.py`对context截断，截断长度在文件中修改。
```python
input_file = 'autodl-tmp/dataset/c1bd30eb76e68b45b319f8069b10b91f.txt'
output_file = 'autodl-tmp/dataset/agr/c1bd30eb76e68b45b319f8069b10b91f.txt'
with open(input_file,'r',encoding='utf-8') as file:
    lines = file.readlines()
res = [line for line in lines if line.strip().replace('\n','')]
li = 12000 #  截断行数
print(len(res))
with open(output_file,'w',encoding='utf-8') as files:
    
    for i in res:
        li -= 1
        if li<=0:
            break
        files.write(i)
```

## MemoRAG推理
在context记忆存储完成后，使用`get_result.py`做最后的推理。jsonl结果文件保存至`autodl-tmp/result`中，使用`autodl-tmp/result/merged.py`文件将12个jsonl合并为一个。

```bash
python autodl-tmp/get_result.py
```
每次执行需要调整对应的context文件名，以访问到数据集中对应的query。
```python
filess = ['660ddc2dc66d64e3f60f3da5b6634b9d.txt', '129d20a7d780e4daacf221d2ff161857.txt', '2948e8343af1d9c6941eeba6067efc0c.txt', '75b9cff8f1ef40c875b7c3d52f9f168f.txt', '7a758123f10a5721b65661694ababbfc.txt', 'f6c2532de0d6c0d7b63f9c3da923fae0.txt', '6301eee8863ab1228e1130c776852439.txt', 'e12308db46ecd7ab54ec6ede5ad1954a.txt', '5c4d27505be8f68d45715fb7060b54ea.txt', 'c1bd30eb76e68b45b319f8069b10b91f.txt', 'e82bc9884f045d9ca167b6526a116eb3.txt', '98a33f1d8593125b320efa556a2c1a39.txt']

file_name = filess[9] #0 1 2 3 4 5 6 7 8 10 11
```




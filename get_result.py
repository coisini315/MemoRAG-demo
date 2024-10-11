import jsonlines
from memorag import MemoRAG, Agent
import os

# 初始化 MemoRAG
model = "gpt-4o-mini"
source = "openai"
api_dict = {
    "api_key": ""
}
agent = Agent(model, source, api_dict)
# print(agent.generate("hi!")) #  test API
pipe = MemoRAG(
    mem_model_name_or_path="autodl-tmp/memorag-mistral",
    ret_model_name_or_path="autodl-tmp/bge-m3", 
    cache_dir="path_to_model_cache",
    customized_gen_model=agent,
)
filess = ['660ddc2dc66d64e3f60f3da5b6634b9d.txt', '129d20a7d780e4daacf221d2ff161857.txt', '2948e8343af1d9c6941eeba6067efc0c.txt', '75b9cff8f1ef40c875b7c3d52f9f168f.txt', '7a758123f10a5721b65661694ababbfc.txt', 'f6c2532de0d6c0d7b63f9c3da923fae0.txt', '6301eee8863ab1228e1130c776852439.txt', 'e12308db46ecd7ab54ec6ede5ad1954a.txt', '5c4d27505be8f68d45715fb7060b54ea.txt', 'c1bd30eb76e68b45b319f8069b10b91f.txt', 'e82bc9884f045d9ca167b6526a116eb3.txt', '98a33f1d8593125b320efa556a2c1a39.txt']

file_name = filess[9] #0 1 2 3 4 5 6 7 8 10 11
# 准备输入文件和输出文件
input_jsonl_file = 'autodl-tmp/dataset/agriculture.jsonl'
output_jsonl_file = 'autodl-tmp/result/'+file_name.split('.')[0]+'.jsonl'
pipe.load("autodl-tmp/cache/agr/"+file_name.split('.')[0], print_stats=True)
context = open("autodl-tmp/dataset/agr/"+file_name).read()
# 打开 jsonl 文件进行读取和写入
with jsonlines.open(input_jsonl_file) as reader, jsonlines.open(output_jsonl_file, mode='w') as writer:
    for obj in reader:
        # 获取当前的 context_id，input 和 answers
        context_id = obj.get('context_id')
        input_text = obj.get('input')
        answers = obj.get('answers', [])
        if context_id != file_name.split('.')[0]:
            continue
        # 通过 MemoRAG 管道回答
        print(context_id)
        query = input_text  # 将答案组合为查询问题
        res = pipe(context=context, query=query, task_type="memorag", max_new_tokens=256)

        # 将回答结果添加到原始对象中
        ans = {
            'context_id' : context_id,
            'input_text' : input_text,
            'answers' : answers,
            'generated_answer': res
        }
            
        # 将结果写入新 jsonl 文件
        writer.write(ans)

print(f"处理完成，结果已保存到 {output_jsonl_file}")




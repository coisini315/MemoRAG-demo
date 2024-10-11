from memorag import MemoRAG, Agent
import os



# Using openai models
model = "gpt-4o-mini"
source = "openai"
api_dict = {
    "api_key": ""
}
agent = Agent(model, source, api_dict)
# print(agent.generate("hi!"))  # Test the API
# Initialize MemoRAG pipeline
pipe = MemoRAG(
    mem_model_name_or_path="autodl-tmp/memorag-mistral",
    ret_model_name_or_path="autodl-tmp/bge-m3", 
    # gen_model_name_or_path="mistral", # Optional: if not specify, use memery model as the generator
    cache_dir="path_to_model_cache",  # Optional: specify local model cache directory
)

files_and_dirs = ['660ddc2dc66d64e3f60f3da5b6634b9d.txt', '129d20a7d780e4daacf221d2ff161857.txt', '2948e8343af1d9c6941eeba6067efc0c.txt', '75b9cff8f1ef40c875b7c3d52f9f168f.txt', '7a758123f10a5721b65661694ababbfc.txt', 'f6c2532de0d6c0d7b63f9c3da923fae0.txt', '6301eee8863ab1228e1130c776852439.txt', 'e12308db46ecd7ab54ec6ede5ad1954a.txt', '5c4d27505be8f68d45715fb7060b54ea.txt', 'c1bd30eb76e68b45b319f8069b10b91f.txt', 'e82bc9884f045d9ca167b6526a116eb3.txt', '98a33f1d8593125b320efa556a2c1a39.txt']
filename = files_and_dirs[9] #0 1 2 3 4 5 6 7 8 10 11
context = open(f"autodl-tmp/dataset/agr/{filename}").read()
print(filename)
# Memorize the context and save to cache
pipe.memorize(context, save_dir="autodl-tmp/cache/agr/"+filename.split('.')[0], print_stats=True)

# # Generate response using the memorized context
# res = pipe(context=context, query=query, task_type="memorag", max_new_tokens=256)
# print(f"MemoRAG generated answer: \n{res}")
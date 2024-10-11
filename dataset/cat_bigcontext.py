input_file = 'autodl-tmp/dataset/c1bd30eb76e68b45b319f8069b10b91f.txt'
output_file = 'autodl-tmp/dataset/agr/c1bd30eb76e68b45b319f8069b10b91f.txt'
with open(input_file,'r',encoding='utf-8') as file:
    lines = file.readlines()
res = [line for line in lines if line.strip().replace('\n','')]
li = 12000
print(len(res))
with open(output_file,'w',encoding='utf-8') as files:
    
    for i in res:
        li -= 1
        if li<=0:
            break
        files.write(i)


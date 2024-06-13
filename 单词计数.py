from collections import Counter

String="itheima itcast python\nitheima python itcast\nbeijing shanghai itheima\nshenzhen guangzhou itheima\nwuhan hangzhou itheima\n " \
       "zhengzhou bigdata itheima\n"

with open('word.txt','w',encoding='UTF-8') as file:
    file.write(String)
with open('word.txt','r',encoding='UTF-8') as file:
    python_num=file.read()
words=python_num.split()
counts=Counter(words)

python_count = counts['python']
print(f"'python' 出现了 {python_count} 次。")
# for word,count in counts.items():
#     print(word,count)
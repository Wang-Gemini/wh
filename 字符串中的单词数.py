def countSegments(s:str)-> int:
    segment_count = 0
    for i in range(len(s)):
        if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
            segment_count += 1
    return segment_count

s=input("请输入一句英语，让我看看它由几个单词组成：\n")
print(countSegments(s))
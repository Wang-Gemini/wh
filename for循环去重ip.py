def one(ips):
    data= set(ips)

    dictionary={}
    for i in ips:
        if i in dictionary:
            dictionary[i] +=1
        else:
            dictionary[i]=1
    sorted_items=sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    # return sorted_items
    return 0

path='attack.csv'
ips=[line.strip() for line in open(path,'r') if line.strip()]
print(one(ips))
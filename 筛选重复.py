import csv

# CSV文件路径
csv_filename = 'C:/Users/Administrator/Desktop/attack.csv'

# 初始化字典来记录IP的出现次数
ip_counts = {}

# 打开CSV文件并读取内容
with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        ip = row[0]  # 假设IP地址在第一列
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

# 将IP地址去重并降序排列出现次数
unique_ips = sorted(ip_counts, key=lambda x: (-ip_counts[x], x))

# 创建两个列表来存储未重复和重复的IP地址及其状态
unique_ips_data = [[ip, "未重复"] for ip in unique_ips if ip_counts[ip] == 1]
duplicate_ips_data = [[ip, f"重复：{ip_counts[ip]}次"] for ip in unique_ips if ip_counts[ip] > 1]

# 合并未重复和重复的IP地址列表，并按出现次数降序排列
sorted_ips_data = duplicate_ips_data + unique_ips_data

# 将新数据写入新的CSV文件
output_filename = 'C:/Users/Administrator/Desktop/attack_sorted.csv'
with open(output_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["IP地址", "状态"])  # 写入标题行
    writer.writerows(sorted_ips_data)  # 写入排序后的数据行

print("数据排序和去重完成，并写入新文件。")
l1 = [1,2,3,2,3,4,5,2,6,7,8]
print(l1)
unique_list = []
for i in l1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
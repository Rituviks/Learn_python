Data = [100,101,4,3,200,205,300,115,201,230,180]
print(Data)
min_val = 100
max_val = 200

for index in range(len(Data)-1,-1,-1):
    if Data[index] < min_val or Data[index] >= max_val:

     del Data[index]

print(Data)

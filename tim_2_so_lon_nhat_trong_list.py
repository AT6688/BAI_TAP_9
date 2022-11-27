number_list = []
n = int(input("nhap so phan tu cua list "))

for i in range(0, n):
    print("nhap phan tu thu", i, )
    item = int(input())
    number_list.append(item)
print("list truoc khi sap xep: ", number_list)
number_list.sort()
print("list truoc khi sap xep: ", number_list)
print("phan tu lon nhat trong list la: ",number_list[-1])
print("phan tu thu hai trong list la: ",number_list[-2])
arraya = [64, 22, 74, 49, 33, 2, 48, 96, 14, 17]
print("field before:", arraya)

serazen = sorted(arraya)
print ("field after:", serazen)

def bubble_sort():
    n = len(arraya)
    for i in range(n-1):
        for j in range (0, n-i-1):
            if arraya[j]>arraya[j+1]:
                arraya[j], arraya[j+1] = arraya[j+1], arraya[j]
                print(arraya)

    return arraya
print(bubble_sort)
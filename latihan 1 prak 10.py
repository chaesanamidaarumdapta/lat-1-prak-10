def findlst(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return findlst(arr, k, low, mid-1)
        else:
            return findlst(arr, k, mid + 1, high)
    else:
        return -1


num = [11,12,13,14,15]
k = int(input("Masukkan angka yang dicari: "))
num.sort()
print(num)
result = findlst(num, k, 0, len(num)-1) + 1

if result != -1:
    print("Elemen ditemukan pada posisi ke-" + str(result))
else:
    print("Elemen tidak ditemukan")
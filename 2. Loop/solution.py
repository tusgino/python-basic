# Cấp độ Dễ

# Bài 1: In các số từ 1 đến 10
print("Bài 1:")
for i in range(1, 11):
    print(i)

# Bài 2: Tính tổng từ 1 đến n
print("\nBài 2:")
n = int(input("Nhập n: "))
total = sum(range(1, n + 1))
print(f"Tổng từ 1 đến {n} là: {total}")

# Bài 3: In bảng cửu chương
print("\nBài 3:")
num = int(input("Nhập số để in bảng cửu chương: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Cấp độ Trung Bình

# Bài 4: Tìm ước số chung lớn nhất (GCD)
print("\nBài 4:")
import math
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"Ước số chung lớn nhất của {a} và {b} là: {math.gcd(a, b)}")

# Bài 5: Đảo ngược chuỗi
print("\nBài 5:")
str_ = input("Nhập chuỗi: ")
print(f"Chuỗi đảo ngược: {str_[::-1]}")

# Bài 6: Kiểm tra số nguyên tố
print("\nBài 6:")
num = int(input("Nhập số để kiểm tra: "))
if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} không phải là số nguyên tố")
            break
    else:
        print(f"{num} là số nguyên tố")
else:
    print(f"{num} không phải là số nguyên tố")

# Cấp độ Khó

# Bài 7: Sắp xếp mảng
print("\nBài 7:")
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f"Mảng sau khi sắp xếp: {arr}")

# Bài 8: Tìm dãy số Fibonacci
print("\nBài 8:")
n_terms = int(input("Nhập số lượng số Fibonacci cần tìm: "))
n1, n2 = 0, 1
count = 0
while count < n_terms:
    print(n1, end=' ')
    n1, n2 = n2, n1 + n2
    count += 1
print()

# Bài 9: Quy hoạch động - Cắt dây để có giá trị lớn nhất
print("\nBài 9:")
def cut_rod(price, n):
    val = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val
    return val[n]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print(f"Giá trị lớn nhất có thể có được là: {cut_rod(arr, size)}")

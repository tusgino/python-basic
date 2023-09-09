# Bài 1:
# Cho danh sách tuple sau:
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# Viết chương trình Python để in danh sách tuple đầu tiên và cuối cùng trong danh sách đã cho.
# Kết quả:
# (1, 2)

# Bài 2:
# Cho danh sách tuple sau:
# [(1, 2, 3), (5, 6, 7), (9, 10, 11), (13, 14, 15)]
# Viết chương trình Python để lặp qua danh sách tuple đã cho, giải nén và in từng giá trị riêng lẻ.
# Viết chương trình Python để lặp qua danh sách tuple đã cho, giải nén và in từng giá trị riêng lẻ và sau đó in tổng của tất cả các giá trị.
# Kết quả:
# 1 2 3 5 6 7 9 10 11 13 14 15
# 6 18 30 42


def bai1():
  # Lời giải
  tuple1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
  print(tuple1[0])
  print(tuple1[-1])

def bai2():
  # Lời giải
  tuple2 = [(1, 2, 3), (5, 6, 7), (9, 10, 11), (13, 14, 15)]
  sums = []

  for i in tuple2:
    a, b, c = i
    print(a, b, c, end=" ")
    sums.append(a + b + c)
  print()
  # Unpack sums và in từng phần tử cách nhau 1 khoảng trắng
  print(*sums)


if __name__ == '__main__':
    bai1()
    bai2()
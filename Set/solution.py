# Bài 1: Tìm các phần tử duy nhất
def unique_elements(lst):
    return set(lst)

# Bài 2: Kiểm tra tập con
def is_subset(A, B):
    return A.issubset(B)

# Bài 3: Thao tác với Set
def set_operations(A, B):
    union_set = A | B
    intersection_set = A & B
    difference_set = A - B
    # return về 1 tuple
    return union_set, intersection_set, difference_set

# Bài 4: Thêm và Xóa phần tử
def add_and_remove_elements(s, add_elem, remove_elem):
    s.add(add_elem)
    s.remove(remove_elem)
    return s

# Bài 5: Đếm số phần tử
def count_elements(s):
    return len(s)

# Bài 6: Tìm giá trị lớn nhất và nhỏ nhất
def find_min_max(s):
    return min(s), max(s)

# Bài 7: Loại bỏ các phần tử trùng lặp từ danh sách
def remove_duplicates(lst):
    return list(set(lst))

# Bài 8: So sánh hai set
def compare_sets(A, B):
    return A == B

# Bài 9: Tìm các phần tử chỉ xuất hiện trong một trong hai set
def unique_in_each_set(A, B):
    return A - B, B - A

# Bài 10: Tạo set từ chuỗi
def set_from_string(string):
    return set(string.lower())

# Test các hàm
if __name__ == "__main__":
    print("Bài 1:", unique_elements([1, 2, 3, 4, 2, 3]))
    print("Bài 2:", is_subset({1, 2}, {1, 2, 3}))
    print("Bài 3:", set_operations({1, 2}, {2, 3}))
    print("Bài 4:", add_and_remove_elements({1, 2, 3}, 4, 1))
    print("Bài 5:", count_elements({1, 2, 3}))
    print("Bài 6:", find_min_max({1, 2, 3, 4, 5}))
    print("Bài 7:", remove_duplicates([1, 2, 3, 4, 2, 3]))
    print("Bài 8:", compare_sets({1, 2, 3}, {1, 2, 3}))
    print("Bài 9:", unique_in_each_set({1, 2, 3}, {3, 4, 5}))
    print("Bài 10:", set_from_string("Hello"))

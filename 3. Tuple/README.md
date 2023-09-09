# Hướng dẫn về Tuple trong Python

## Mục lục

1. [Đặc điểm của Tuple](#đặc-điểm-của-tuple)
2. [Cú pháp](#cú-pháp)
3. [Truy cập phần tử](#truy-cập-phần-tử)
4. [Cắt Tuple](#cắt-tuple)
5. [Nối Tuple](#nối-tuple)
6. [Đếm và Tìm kiếm](#đếm-và-tìm-kiếm)
7. [Unpacking](#unpacking)
8. [Lưu ý](#lưu-ý)

---

## Đặc điểm của Tuple

1. **Không thể thay đổi (Immutable)**: Một khi đã tạo tuple, bạn không thể thêm, xóa hoặc sửa đổi các phần tử trong tuple.
2. **Có thứ tự (Ordered)**: Các phần tử trong tuple có thứ tự, và bạn có thể truy cập chúng thông qua chỉ số.
3. **Cho phép trùng lặp (Duplicate)**: Tuple có thể có các phần tử giống nhau.
4. **Có thể chứa nhiều kiểu dữ liệu**: Tuple có thể chứa số nguyên, số thực, chuỗi, và cả các kiểu dữ liệu phức tạp khác như list, set, và tuple khác.

## Cú pháp

```python
my_tuple = (1, 2, 3, "Hello", 4.5)
```

## Truy cập phần tử

```python
first_element = my_tuple[0]  # Truy cập phần tử đầu tiên
last_element = my_tuple[-1]  # Truy cập phần tử cuối cùng
```

## Cắt Tuple

```python
sub_tuple = my_tuple[1:4]  # Lấy các phần tử từ chỉ số 1 đến 3
```

## Nối Tuple

```python
new_tuple = my_tuple + (6, 7, 8)
```

## Đếm và Tìm kiếm

```python
count = my_tuple.count(1)  # Đếm số lần xuất hiện của phần tử 1
index = my_tuple.index("Hello")  # Tìm chỉ số của phần tử "Hello"
```

## Unpacking

```python
a, b, c, d, e = my_tuple  # Gán các giá trị của tuple vào các biến
```

## Lưu ý

- Vì tuple là immutable, nên chúng thường được sử dụng trong các trường hợp cần đảm bảo dữ liệu không bị thay đổi, ví dụ như làm key cho dictionary.

# Ví dụ thực tế về việc sử dụng Tuple trong Python

## 1. Làm Key cho Dictionary

Vì tuple là immutable, chúng có thể được sử dụng làm key trong dictionary, điều này không thể làm với list.

```python
coordinate_dict = { (40.7128, -74.0060): 'New York', (34.0522, -118.2437): 'Los Angeles' }
```

## 2. Trả về nhiều giá trị từ một hàm

Tuple cho phép bạn trả về nhiều giá trị từ một hàm.

```python
def min_max(arr):
    return min(arr), max(arr)

result = min_max([1, 2, 3, 4, 5])
print(result)  # Output: (1, 5)
```

## 3. Đóng gói và Giải nén Dữ liệu

Tuple giúp đóng gói nhiều giá trị vào một biến duy nhất.

```python
student = ("TuGiNo", 20, "Software Engineer")

# Unpacking
name, age, major = student
```

## 4. Duy trì Thứ tự

Khi bạn cần một danh sách không thay đổi và duy trì thứ tự của các phần tử, tuple là lựa chọn tốt.

```python
directions = ('Da Nang', 'Gia Lai', 'Sai Gon', 'Ha Noi')
```

## 5. Đảm bảo An toàn Dữ liệu

Khi bạn muốn đảm bảo rằng dữ liệu không bị thay đổi trong suốt chương trình, sử dụng tuple.

```python
config = ('192.168.1.1', 8080)
```

```python
Author: Tusgino
```

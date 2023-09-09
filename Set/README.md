## Sets trong Python

Set là một kiểu dữ liệu trong Python dùng để lưu trữ các giá trị không có thứ tự và không trùng lặp. Set được sử dụng trong các trường hợp cần thực hiện các thao tác như hợp nhất, giao, hiệu, và kiểm tra tính phần tử.

### Đặc điểm của Set

1. **Không có thứ tự (Unordered)**: Các phần tử trong set không có thứ tự.
2. **Không trùng lặp (Unique)**: Mỗi phần tử trong set là duy nhất.
3. **Không thể thay đổi (Immutable)**: Phần tử trong set không thể thay đổi, nhưng set có thể thêm hoặc xóa phần tử.
4. **Có thể chứa nhiều kiểu dữ liệu**: Set có thể chứa số nguyên, số thực, chuỗi, và cả các kiểu dữ liệu không thay đổi khác như tuple.

### Cú pháp

```python
my_set = {1, 2, 3, "Hello"}
```

### Thêm và Xóa Phần Tử

```python
my_set.add(4)  # Thêm phần tử 4 vào set
my_set.remove("Hello")  # Xóa phần tử "Hello" khỏi set
```

### Thao tác với Set

```python
A = {1, 2, 3}
B = {3, 4, 5}

union_set = A | B  # Hợp nhất A và B {1,2,3,4,5}
intersection_set = A & B  # Giao của A và B {3}
difference_set = A - B  # Hiệu của A so với B {1,2}
difference_set_2 = B - A  # Hiệu của B so với A {4,5}
```

## Ví dụ thực tế

### 1. Loại bỏ các phần tử trùng lặp

```python
my_list = [1, 2, 2, 3, 4, 3, 5]
unique_elements = set(my_list)
```

### 2. Kiểm tra tính phần tử

```python
if 1 in unique_elements:
    print("1 trong set")
```

### 3. Thao tác với tập hợp dữ liệu

Giả sử bạn có hai danh sách người dùng của hai ứng dụng khác nhau và bạn muốn tìm ra những người dùng chung giữa hai ứng dụng.

```python
app1_users = {'Tu', 'Linh', 'Trung'}
app2_users = {'Linh', 'Vu', 'Trung'}
common_users = app1_users & app2_users
# {'Linh', 'Trung'}
# Sẽ không trả về đúng thứ tự
```

### 4. Tính toán thống kê

#### Mô tả

Set trong Python có thể được sử dụng để thực hiện nhiều loại phép tính thống kê, như tìm các phần tử duy nhất trong một tập dữ liệu, kiểm tra xem một tập hợp có phải là tập con của tập hợp khác hay không, và tìm tập hợp giao nhau giữa hai tập hợp.

#### Ví dụ

##### Tìm các phần tử duy nhất

Giả sử bạn có một danh sách điểm số của học sinh và bạn muốn tìm các điểm số duy nhất.

```python
scores = [90, 85, 77, 85, 90, 88, 92, 85, 77, 88]
unique_scores = set(scores)
print("Điểm rèn luyện:", unique_scores)
```

Kết quả: `Điểm rèn luyện: {77, 85, 88, 90, 92}`

##### Kiểm tra tập con

Giả sử bạn có một tập hợp các sản phẩm trong kho và một tập hợp các sản phẩm đã bán. Bạn muốn kiểm tra xem tất cả các sản phẩm đã bán có trong kho hay không.

```python
inventory = {'apple', 'banana', 'orange', 'mango'}
sold = {'apple', 'banana'}
is_subset = sold.issubset(inventory)
print("All sold products are in inventory:", is_subset)
```

Kết quả: `All sold products are in inventory: True`

##### Tìm tập hợp giao nhau

Giả sử bạn có hai tập hợp dữ liệu về khách hàng của hai cửa hàng khác nhau và bạn muốn tìm ra những khách hàng chung.

```python
store1_customers = {'Alice', 'Bob', 'Charlie'}
store2_customers = {'Bob', 'Dave', 'Eve'}
common_customers = store1_customers & store2_customers
print("Common customers:", common_customers)
```

Kết quả: `Common customers: {'Bob'}`

Như vậy, set có thể được sử dụng trong nhiều tình huống thống kê và phân tích dữ liệu.

### 5. Quản lý quyền truy cập

Set có thể được sử dụng để quản lý các quyền truy cập trong ứng dụng, ví dụ như quyền đọc, quyền ghi, quyền chỉnh sửa, ...

```python
user_permissions = {'read', 'write'}
required_permissions = {'read'}

if required_permissions.issubset(user_permissions):
    print("You have the required permissions.")
```

```python
Author: Tusgino
```

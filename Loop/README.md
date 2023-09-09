### Vòng lặp `while` trong Python

#### Mô tả

Vòng lặp `while` được sử dụng để lặp đi lặp lại một khối mã cho đến khi điều kiện cho trước trở thành `False`.

#### Cú pháp

```python
while điều_kiện:
    # Khối mã để thực hiện
```

#### Ví dụ

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

---

### Vòng lặp `for` trong Python

#### Mô tả

Vòng lặp `for` được sử dụng để lặp qua các phần tử của một đối tượng lặp (ví dụ: danh sách, tuple, chuỗi, set, dictionary).

#### Loại `for` trong Python

1. **For thông thường**: Lặp qua các phần tử của một đối tượng lặp.

   ```python
   for item in iterable:
       # Khối mã để thực hiện
   ```

   Ví dụ:

   ```python
   for i in [1, 2, 3]:
       print(i)
   ```

2. **For với `enumerate`**: Lặp qua các phần tử và chỉ số của chúng.

   ```python
   for index, item in enumerate(iterable):
       # Khối mã để thực hiện
   ```

   Ví dụ:

   ```python
   for index, value in enumerate(["a", "b", "c"]):
       print(f"Index: {index}, Value: {value}")
   ```

3. **For với `zip`**: Lặp qua nhiều đối tượng lặp cùng một lúc.

   ```python
   for item1, item2 in zip(iterable1, iterable2):
       # Khối mã để thực hiện
   ```

   Ví dụ:

   ```python
   for a, b in zip([1, 2, 3], ["a", "b", "c"]):
       print(f"a: {a}, b: {b}")
   ```

4. **For với `items` (cho dictionary)**: Lặp qua các cặp key-value của một dictionary.

   ```python
   for key, value in dictionary.items():
       # Khối mã để thực hiện
   ```

   Ví dụ:

   ```python
   for key, value in {"a": 1, "b": 2}.items():
       print(f"Key: {key}, Value: {value}")
   ```

5. **For với `range`**: Lặp qua một dãy số.
   ```python
   for i in range(start, stop, step):
       # Khối mã để thực hiện
   ```
   Ví dụ:
   ```python
   for i in range(0, 10, 2):
       print(i)
   ```

#### Nested For Loop (Vòng For lồng nhau)

Bạn cũng có thể sử dụng vòng `for` lồng nhau để xử lý các tình huống phức tạp hơn.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

```python
Author: Tusgino
```

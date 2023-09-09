# Câu lệnh If-Else trong Python:

## Giới thiệu

Trong Python, câu lệnh `if-else` là một cơ chế điều khiển luồng cơ bản, cho phép chương trình thực hiện các khối mã khác nhau dựa trên điều kiện nhất định. README này nhằm cung cấp một hiểu biết sâu rộng về cách hoạt động của câu lệnh `if-else` trong Python, cú pháp của nó, và các trường hợp sử dụng khác nhau. Dù bạn là người mới học lập trình hay là một nhà phát triển có kinh nghiệm, việc hiểu rõ câu lệnh `if-else` là rất quan trọng để viết mã hiệu quả và dễ đọc.

## Mục lục

1. [Cú pháp](#cú-pháp)
2. [Ví dụ cơ bản](#ví-dụ-cơ-bản)
3. [If-Else lồng nhau](#if-else-lồng-nhau)
4. [Câu lệnh Elif](#câu-lệnh-elif)
5. [Toán tử ba ngôi](#toán-tử-ba-ngôi)
6. [Các lỗi thường gặp](#các-lỗi-thường-gặp)
7. [Thực hành tốt nhất](#thực-hành-tốt-nhất)
8. [Kết luận](#kết-luận)

## Cú pháp

Cú pháp cơ bản của một câu lệnh `if-else` trong Python như sau:

```python
if condition:
    # Khối mã sẽ được thực hiện nếu condition là True
else:
    # Khối mã sẽ được thực hiện nếu condition là False
```

- `condition`: Một biểu thức boolean đánh giá thành `True` hoặc `False`.
- `:` (dấu hai chấm): Chỉ ra bắt đầu của khối mã sẽ được thực hiện dựa trên điều kiện.
- Thụt lề: Python sử dụng thụt lề để xác định các khối mã. Các mã thụt lề dưới `if` và `else` sẽ được thực hiện dựa trên điều kiện.

## Ví dụ cơ bản

### Ví dụ 1: Kiểm tra số chẵn hay lẻ

```python
num = 5

if num % 2 == 0:
    print("Chẵn")
else:
    print("Lẻ")
```

### Ví dụ 2: So sánh hai số

```python
a = 10
b = 20

if a > b:
    print("a lớn hơn")
else:
    print("b lớn hơn")
```

## If-Else lồng nhau

Bạn có thể đặt một câu lệnh `if-else` bên trong một câu lệnh `if-else` khác. Điều này được gọi là lồng nhau.

### Ví dụ: Hệ thống chấm điểm

```python
score = 85

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        print("C")
```

## Câu lệnh Elif

Câu lệnh `elif` (else-if) cho phép bạn kiểm tra nhiều điều kiện mà không cần lồng nhau.

### Ví dụ: Hệ thống chấm điểm với `elif`

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

## Toán tử ba ngôi

Python cũng cung cấp một cú pháp ngắn gọn cho `if-else` được biết đến là toán tử ba ngôi.

```python
x = 10
y = "Chẵn" if x % 2 == 0 else "Lẻ"
```

## Các lỗi thường gặp

1. **Quên dấu hai chấm**: Luôn nhớ đặt dấu hai chấm vào cuối dòng `if` và `else`.
2. **Lỗi thụt lề**: Đảm bảo thụt lề các khối mã đúng cách.

## Thực hành tốt nhất

1. **Code dễ đọc**: Giữ cho các điều kiện của bạn đơn giản để dễ đọc mã.
2. **Tránh lồng nhau sâu**: Quá nhiều câu lệnh `if-else` lồng nhau có thể làm cho mã khó theo dõi.

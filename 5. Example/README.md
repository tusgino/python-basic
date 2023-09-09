### Bài Tập: Quản Lý Thư Viện Đơn Giản

#### Mô Tả:

Bạn sẽ xây dựng một ứng dụng console để quản lý thư viện. Ứng dụng này sẽ có các chức năng cơ bản như thêm sách, xóa sách, tìm kiếm sách và hiển thị danh sách sách.

#### Yêu Cầu:

1. **Thêm Sách**: Người dùng có thể thêm thông tin về sách mới, bao gồm tên sách, tác giả, và năm xuất bản.
2. **Xóa Sách**: Người dùng có thể xóa sách dựa trên tên sách.
3. **Tìm Kiếm Sách**: Người dùng có thể tìm kiếm sách dựa trên tên sách hoặc tác giả.
4. **Hiển Thị Danh Sách Sách**: Người dùng có thể xem danh sách tất cả các sách hiện có trong thư viện.

#### Cấu Trúc Dữ Liệu:

Bạn có thể sử dụng danh sách (list) của từ điển (dictionary) để lưu trữ thông tin sách. Mỗi từ điển sẽ chứa các khóa như `name`, `author`, và `year`.

```python
library = [
    {'name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'name': '1984', 'author': 'George Orwell', 'year': 1949},
    # ...
]
```

#### Giao Diện Người Dùng:

Ứng dụng sẽ có một menu chính, cho phép người dùng chọn các chức năng.

```plaintext
=== Library Management ===
1. Add Book
2. Delete Book
3. Search Book
4. Display Books
5. Exit
```

#### Mã Khởi Đầu:

```python
def main():
    library = []
    while True:
        print("=== Library Management ===")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Implement Add Book
        elif choice == '2':
            # Implement Delete Book
        elif choice == '3':
            # Implement Search Book
        elif choice == '4':
            # Implement Display Books
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

```
Author: Tusgino
```

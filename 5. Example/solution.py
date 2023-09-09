# Ứng dụng Quản Lý Thư Viện bằng Python

def them_sach(thu_vien):
    ten = input("Nhập tên sách: ")
    tac_gia = input("Nhập tên tác giả: ")
    nam_xb = int(input("Nhập năm xuất bản: "))
    thu_vien.append({'ten': ten, 'tac_gia': tac_gia, 'nam_xb': nam_xb})
    print(f"Sách '{ten}' đã được thêm thành công.")

def xoa_sach(thu_vien):
    ten = input("Nhập tên sách cần xóa: ")
    for sach in thu_vien:
        if sach['ten'] == ten:
            thu_vien.remove(sach)
            print(f"Sách '{ten}' đã được xóa thành công.")
            return
    print(f"Không tìm thấy sách '{ten}'.")

def tim_sach(thu_vien):
    tu_khoa = input("Nhập tên sách hoặc tác giả cần tìm: ")
    sach_tim_thay = [sach for sach in thu_vien if tu_khoa.lower() in sach['ten'].lower() or tu_khoa.lower() in sach['tac_gia'].lower()]
    if sach_tim_thay:
        print("Các sách tìm thấy:")
        for sach in sach_tim_thay:
            print(f"{sach['ten']} của {sach['tac_gia']} (Năm {sach['nam_xb']})")
    else:
        print("Không tìm thấy sách nào.")

def hien_thi_sach(thu_vien):
    if not thu_vien:
        print("Thư viện không có sách.")
        return
    print("Danh sách các sách:")
    for sach in thu_vien:
        print(f"{sach['ten']} của {sach['tac_gia']} (Năm {sach['nam_xb']})")

def main():
    thu_vien = []
    while True:
        print("\\n=== Quản Lý Thư Viện ===")
        print("1. Thêm Sách")
        print("2. Xóa Sách")
        print("3. Tìm Sách")
        print("4. Hiển Thị Sách")
        print("5. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            them_sach(thu_vien)
        elif lua_chon == '2':
            xoa_sach(thu_vien)
        elif lua_chon == '3':
            tim_sach(thu_vien)
        elif lua_chon == '4':
            hien_thi_sach(thu_vien)
        elif lua_chon == '5':
            print("Thoát ứng dụng.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()

print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
def tinh_so_tien_tai_khoan():
#Định nghĩa một hàm có tên tinh_so_tien_tai_khoan không nhận tham số nào. Hàm này sẽ tính số tiền trong tài khoản sau các giao dịch
    so_du = 0
    #Khởi tạo biến so_du lưu số dư tài khoản, bắt đầu từ 0 (tức là tài khoản rỗng)
    n = int(input("Nhập số lượng giao dịch: "))
    # Yêu cầu người dùng nhập vào số lượng giao dịch mà họ muốn thực hiện (số nguyên n).
    for _ in range(n):
    #vòng lặp lặp qua n giao dịch.
        giao_dich = input("Nhập giao dịch (D/W số_tiền): ").split()
        """Yêu cầu người dùng nhập thông tin giao dịch. Người dùng phải nhập một chuỗi có dạng D/W số_tiền, 
        trong đó D là nạp tiền (Deposit), W là rút tiền (Withdraw), và số_tiền là số tiền giao dịch."""
        # .split(): Tách chuỗi nhập vào thành một danh sách các phần tử (dùng dấu cách để tách).
        loai_giao_dich = giao_dich[0]
        # Lấy phần tử đầu tiên trong danh sách giao_dich, là loại giao dịch (D hoặc W).
        so_tien = int(giao_dich[1])
        #Lấy phần tử thứ hai trong danh sách giao_dich, là số tiền giao dịch, và chuyển nó thành số nguyên (int) để thực hiện các phép toán.
        if loai_giao_dich == 'D':
        #if loai_giao_dich == 'D':: Nếu loại giao dịch là nạp tiền (D), cộng số tiền vào so_du (số dư tài khoản).
            so_du += so_tien
        elif loai_giao_dich == 'W':
        #elif loai_giao_dich == 'W':: Nếu loại giao dịch là rút tiền (W), trừ số tiền từ so_du (số dư tài khoản).
            so_du -= so_tien
    print(f"Số tiền thực của tài khoản là: {so_du}")
tinh_so_tien_tai_khoan()
#Gọi hàm tinh_so_tien_tai_khoan() để thực thi toàn bộ chương trình.
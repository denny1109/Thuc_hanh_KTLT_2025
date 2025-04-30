print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
chuoi = input('Nhap chuoi: ')
#Lệnh input() yêu cầu người dùng nhập một chuỗi từ bàn phím,chuỗi sẽ được lưu vào biến chuoi
chuoi_moi = ''.join([ki_tu for ki_tu in chuoi if not ki_tu.isdigit()])
"""Dòng này tạo một chuỗi mới tên là chuoi_moi,Nó duyệt qua từng ký tự trong chuỗi chuoiNếu 
ký tự không phải là số thì giữ lại cuối cùng nối các ký tự thành chuỗi mới
.isdigit() là một hàm có sẵn trong Python, được dùng với chuỗi để kiểm tra xem một ký tự 
(hoặc chuỗi) có phải là chữ số hay không
''.join() là một hàm dùng để nối các phần tử (chuỗi) trong một danh sách (hoặc bất kỳ kiểu 
lặp nào) thành một chuỗi duy nhất"""
print('Chuoi sau khi loai b chu so:', chuoi_moi)

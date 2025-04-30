print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")

s= input('nhap chuoi:')#Lệnh input() yêu cầu người dùng nhập một chuỗi từ bàn phím,chuỗi sẽ được lưu vào biến s
for ch in s:#Dùng vòng lặp for để duyệt từng ký tự trong chuỗi s
    if ch not in(' ','\t'):
    #Kiểm tra nếu ch không phải là khoảng trắng ' ' hoặc tab '\t', thì mới in ra,Nếu ký tự là space hoặc tab, thì bỏ qua
     print(ch)
 

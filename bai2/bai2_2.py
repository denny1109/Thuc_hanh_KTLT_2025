import math # import math: nhập thư viện toán học 
x1=int(input("vui lòng nhập x1: ")) 
y1=int(input("vui lòng nhập y1: "))
x2=int(input("vui lòng nhập x2: "))
y2=int(input("vui lòng nhập y2: "))
# int: chuyển đổi từ xâu qua số
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
# math.sqrt: dùng để tính căn bậc 2 của cái trong ngoặc
# **: ký hiệu của mũ
print("khoảng cách giữ hai điểm là:",d)
print("Sinh viên: Phạm Trọng Phúc")
print("MSSV: 235752020710029") 
# print: in ra màn hình 
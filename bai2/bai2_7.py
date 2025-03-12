n=int(input("Nhập vào một số:"))
#int dùng để chuyển đổi xâu sang số
d=dict() #dict() là một hàm được dùng để tạo từ điển. 
#Từ điển là một kiểu dữ liệu dạng ánh xạ gồm cặp khóa (key) - giá trị (value).
for i in range(1,n+1):
    d[i]=i*i
# range tạo số liên tiếp trong khoảng
# for vòng lặp  
"""vòng lặp for với i là các số tiếp từ 1 đến n bao gồm cả n thì sẽ thêm vào từ 
điển với key là i và giá trị là i*i""" 
print(d)
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
# print: in ra màn hình
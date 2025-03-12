str=input("Vui lòng nhập xâu: ")
""" tạo thư viện mới"""
dict={}
"""Vòng lặp for i in str: sẽ duyệt từng ký tự i trong chuỗi str.
str.count(i) đếm số lần xuất hiện của ký tự i trong str.
dict[i] = str.count(i) sẽ gán số lần xuất hiện của i vào từ điển với i là khóa."""
for i in str:
    dict[i]=str.count(i)
print (dict)
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
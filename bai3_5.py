a="Hello Guy!" #gán biến toàn cục a bằng xâu hello guy
def say():# khai báo hàm say
    global a #chuyển biến a từ cục bộ lên toàn cục
    a="Vinh University" # gán biến cụ bộ a bằng xâu Vinh University
    print(a)
say() #gọi hàm say với biến cục bộ(biến toàn cục mới)
print(a) # in ra màn hình với a là biến toàn cụ mới, biến toàn cục mới là biến cụ bộ
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
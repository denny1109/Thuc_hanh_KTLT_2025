import re
"""import re: nhập thư viện dùng để làm việc với biểu thức chính quy (regex), rất hữu 
ích để kiểm tra mẫu ký tự trong chuỗi (như có chữ, số, ký tự đặc biệt, v.v.)"""
value=[]
#Tạo một danh sách rỗng value để lưu các mật khẩu hợp lệ
items=[x for x in input("Nhập mật khẩu: ").split(',')]
# Yêu cầu người dùng nhập nhiều mật khẩu, cách nhau bằng dấu phẩy.Dùng .split(',') để tách thành danh sách items
for p in items:
#Duyệt từng mật khẩu p trong danh sách items
    if len(p)<6 or len(p)>12:
    #Nếu mật khẩu ngắn hơn 6 ký tự hoặc dài hơn 12, thì bỏ qua
        continue
    else:
        pass
    if not re.search("[a-z]",p):
    #Nếu không có chữ thường, bỏ qua
        continue
    elif not re.search("[0-9]",p):
    #Nếu không có số, bỏ qua
        continue
    elif not re.search("[A-Z]",p):
    #Nếu không có chữ hoa, bỏ qua
        continue
    elif not re.search("[$#@]",p):
    #Nếu không có ký tự đặc biệt $, #, hoặc @, bỏ qua
        continue
    elif re.search("\s",p):
    #Nếu có khoảng trắng, bỏ qua
        continue
    else:
        pass
    value.append(p)
    #Thêm mật khẩu hợp lệ vào danh sách value.
print(",".join(value))
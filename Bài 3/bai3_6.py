def get_sum(*num): #khai báo một hàm tên là get_sum
    tmp=0 #Tạo một biến tmp dùng để lưu trữ tổng tạm thời của các số
    for i in num:#Vòng lặp for duyệt qua từng phần tử trong num (tuple chứa các số được truyền vào hàm).
    #Mỗi lần lặp, i sẽ giữ giá trị của từng phần tử trong num
        tmp+=i #viết tắt của tmp = tmp + i,có nghĩa là cộng giá trị i hiện tại vào biến tmp
    return tmp #Sau khi đã cộng hết tất cả các số trong num, kết quả tổng sẽ được trả về
result=get_sum(1,2,3,4,5) #Gọi hàm get_sum với các số từ 1 đến 5,Tổng là 15, nên result sẽ có giá trị là 15
print(result)
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
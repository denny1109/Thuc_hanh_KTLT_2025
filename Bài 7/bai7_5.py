print("sinh vien: Phạm Trọng Phúc")
print("Mssv: 235752020710029")
def file_append_and_read(fname):
#Định nghĩa một hàm có tên file_append_and_read, nhận đối số fname là tên hoặc đường dẫn tệp.
    with open(fname, "a") as myfile:
    #Mở tệp với tên fname ở chế độ append ("a") – tức là ghi thêm vào cuối tệp, không làm mất nội dung cũ.
    #Biến myfile đại diện cho tệp đang mở.
    #Câu lệnh with giúp tự động đóng tệp sau khi đọc xong, tránh rò rỉ tài nguyên.
        myfile.write("29 bachlieu\n")
        myfile.write("11092005\n")
        #Ghi hai dòng mới vào cuối tệp:Dòng đầu: "29 bachlieu\n" (bao gồm ký tự xuống dòng \n) Dòng sau: "11092005\n"
    with open(fname, "r") as txt:
    #Mở lại tệp ở chế độ đọc ("r") để xem toàn bộ nội dung sau khi đã thêm dữ liệu.
        print(txt.read())
        #Đọc và in ra toàn bộ nội dung của tệp, bao gồm cả những dòng vừa thêm.
file_append_and_read('bài 7/phuc.txt')
#Gọi hàm và yêu cầu đọc 1 dòng đầu tiên của tệp 'bài 7/phuc.txt'.

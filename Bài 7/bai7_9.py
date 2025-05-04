print("sinh vien: Phạm Trọng Phúc")
print("Mssv: 235752020710029")
def copy_file_content(source_file, destination_file):
#Định nghĩa một hàm tên là copy_file_content, nhận vào hai đối số:
#source_file: đường dẫn đến tệp nguồn (nơi chứa nội dung gốc cần sao chép).
#destination_file: đường dẫn đến tệp đích (nơi sẽ chứa bản sao của nội dung).
    with open(source_file, 'r') as src:
    #Mở tệp nguồn (source_file) ở chế độ đọc ('r').
    #Từ khóa with giúp đảm bảo rằng tệp sẽ tự động được đóng sau khi khối lệnh kết thúc.
    #Biến src là một đối tượng file đại diện cho tệp nguồn.
        with open(destination_file, 'w') as dest:
        #Mở tệp đích (destination_file) ở chế độ ghi ('w'), nghĩa là:Nếu tệp đã tồn tại, nội dung cũ sẽ bị xóa và ghi lại từ đầu.,Nếu tệp chưa tồn tại, sẽ tự động được tạo mới.
        #Biến dest là đối tượng file đại diện cho tệp đích.
            content = src.read() 
            #Đọc toàn bộ nội dung từ tệp nguồn (src) và lưu vào biến content. 
            dest.write(content)
            #Ghi nội dung vừa đọc được (content) vào tệp đích (dest). 
source_file_name = 'bài 7/phuc.txt' #Gán chuỗi 'bài 7/phuc.txt' (đường dẫn đến tệp nguồn) cho biến source_file_name.
destination_file_name = 'bài 7/destination.txt'#Gán chuỗi 'bài 7/destination.txt' (đường dẫn đến tệp đích) cho biến destination_file_name.  
copy_file_content(source_file_name, destination_file_name)
#Gọi hàm copy_file_content để sao chép nội dung từ tệp nguồn sang tệp đích.
print(f"Nội dung của tệp '{source_file_name}' đã được sao chép sang tệp '{destination_file_name}'.")
#In ra thông báo xác nhận quá trình sao chép đã hoàn tất, sử dụng f-string để chèn tên các tệp vào thông báo.

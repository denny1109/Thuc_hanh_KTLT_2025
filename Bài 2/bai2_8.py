a,b=1,2 
"""1 và 2 là 2 số đầu của dãy fibonaci"""
tong = 0
print(a,end=" ")
while (b <= 4000000-1):
    if a%2==0:
        tong +=a
    a,b=b,a+b
    print(a,end=" ")
    """ vòng lặp while b bé thua hoặc bằng 4000000-1 thì a trước đó sẽ được thay 
    bằng b và b sẽ được thay bằng a+b lặp đi lặp lại cho đến khi b lơn hơn 4000000-1 thì dừng 
    rồi in ra số đầu tiên cho đến số cuối cùng và nếu số a chia 2 dư o thì cộng số đó vào tổng"""
print("\n tổng của các số chẵn trong dãy fibonaci: ",tong)
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")
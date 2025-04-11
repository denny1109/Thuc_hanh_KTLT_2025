print("Phạm Trọng Phúc")
print("MSSV:23575202710029")

""" Chương trình hoạt động như một cái máy tính bỏ túi bình thường  có thể cộng trù nhân chia """
# This function adds two numbers  
def tong(x, y): 
 return x + y 
# This function subtracts two numbers  
def hieu(x, y): 
 return x - y 
# This function multiplies two numbers 
def tich(x, y): 
 return x * y 
# This function divides two numbers 
def thuong(x, y): 
 return x / y 
print("Select operation.") 
print("1.tong") 
print("2.hieu") 
print("3.tich") 
print("4.thuong") 
# Take input from the user  
choice = input("Enter choice(1/2/3/4):") 
num1 = int(input("Vui lòng nhập số đầu tiên: ")) 
num2 = int(input("Vui lòng nhập số thứ hai: ")) 
if choice == '1': 
 print(num1,"+",num2,"=", tong(num1,num2)) 
elif choice == '2': 
 print(num1,"-",num2,"=", hieu(num1,num2)) 
elif choice == '3': 
 print(num1,"*",num2,"=", tich(num1,num2)) 
elif choice == '4': 
 print(num1,"/",num2,"=", thuong(num1,num2)) 
else: 
 print("Invalid input") 

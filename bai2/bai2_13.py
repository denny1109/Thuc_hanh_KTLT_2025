import math
a=int(input("vui lòng nhập a: "))
b=int(input("vui lòng nhập b: "))
c=int(input("vui lòng nhập c: "))
if a==0:
    x=-c/b
    print("nghiệm của phương trình là:",x)
    """ nếu a=0 thì phương trình trở thành phương trình bậc nhất bx+c=0 khi đó x=-c/a"""
else:
    """ nếu a khác 0 tính denta = b^2-4ac""" 
    denta=b**2-4*a*c
    if denta<0:
        """nếu denta bé hơn 0 thì in ra màn hình ptinh vô nghiệm"""
        print("phương trình vô nghiệm")
    elif denta==0:
        """denta=0 phương trình có nghiệm kép x=b/2a tính và in ra màn hình"""
        x=-b/2*a
        print("Phương trình có nghiệm kép:",x)
    else:
        """denta>0 có 2 nghiệm phân biệt x1,x2"""
        x1=(-b+math.sqrt(denta))/2
        x2=(-b-math.sqrt(denta))/2
        print("Phương trình có hai nghiệm phân biệt: ",x1,",",x2)
print("Sinh viên: Phạm Trọng Phúc")
print(" MSSV: 235752020710029")

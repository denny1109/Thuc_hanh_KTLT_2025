print("Phạm Trọng Phúc")
print("MSSV:235752021710029")

import math 
pos = [0,0] 
while True: 
 s = input("Vui lòng nhập lệnh di chuyển: ") 
 if not s: 
  break 
 movement = s.split(" ") 
 direction = movement[0] 
 steps = int(movement[1]) 
 if direction=="UP": 
  pos[0]+=steps 
 elif direction=="DOWN": 
  pos[0]-=steps 
 elif direction=="LEFT": 
  pos[1]-=steps
 elif direction=="RIGHT": 
  pos[1]+=steps 
 else: 
  pass 
###################### 
print ("Khoagr cách từ hiện tại vị trí đầu tiên là: ",int(round(math.sqrt(pos[1]**2+pos[0]**2))))

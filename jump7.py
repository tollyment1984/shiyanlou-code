#number = range(1,101)

for a in range(1,101):
    if a%7==0:
       # print(' X ')
        continue
    elif a % 10 ==  7:
       # print(' XX ') 
        continue
    elif a // 10 == 7:
       # print(' ** ')    
        continue
    else: 
        print(a)
print("*********"+str(a))

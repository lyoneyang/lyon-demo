#打印乘法口诀
a=1
b=1
while b<=9:
    for a in range(1,10):
        print(str(a),"×",str(b),"=",str(a*b)+"  ",end="")
    print("\n")
    b=b+1
#第二种打印乘法口诀方法
f=0
for i in range(1,10):
    for g in range(1,i+1):
        print(i,"×",g,"=",i*g,"  ",end="")
        f+=1
    print("\n")
print(f)







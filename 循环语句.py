# 打印10次"我爱刘洋"
for a in [1,1,1,1,1,1,1,1,1,1]:
    print('我爱刘洋')
print('------------------')

#通过Range函数
for c in range(1,10):
    print('我爱python')
print('------------------')

# while 函数
b=0
while b < 10:
    print('我爱刘洋')
    b=b+1

# range三个函数的情况
d=range(1,4,2)
print(d)

for e in range(2,20,3):
    print(e)
print('------------------')
# range函数打印字符串
f="打发撒来访量水电费拉圣诞福利"
for i in range(5):
    print(f[i])
print('------------------')
print(f[2])
print('------------------')
#从1+100的和。
f=0
for t in range(1,101):
    f=f+t
print(f)

#打印1-20内的偶数
#for语句
i=0
for i in range(1,21):
    if i%2==0:
        print("我是偶数",i)
        break
        print('我真厉害')
#while循环
i=0
while i<21:
    i+=1
    if i%2==0:
        print('while语句下的我是偶数',i)








print('hello word!')
a=1
for a in range(1,11):
    if a%3==0:
        continue
    else:
        print(a)
print('和平')
b=1
while b<40:
    b=b+1
    if b%4==0 or b%10==4 or b%4==10:
        continue
    else:
        print(b)
        str('12345')
c=input('请输入你的名称：')
d=int(input('请输入你的年龄：'))
if c=='张珊' and d=='10':
    print('您是个优秀且快乐的男生')
else:
    print('对不起，我还不认识你')

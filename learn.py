print("Let's go!")
print('Let\'s go!')
print('Let\'s say:''"Hello world！"')
a='Let\'s say:'
b='"Hello world！"'
print(a+b)
c=input('请输入你l的名字：')
print(c)

a=float(input('请输入第一位小朋友身高：'))
b=float(input('请输入第二位小朋友身高：'))
c=float(input('请输入第三位小朋友身高：'))
if a>b and a>c:
    print('最高的小朋友是第一位')
elif b>a and b>c:
    print("最高的小朋友是第二位")
elif c>a and c>b:
    print("最高的小朋友是第三位")
else:
    print('没有最高的小朋友')


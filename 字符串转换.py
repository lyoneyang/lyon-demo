#根据身高体重测量体脂
h=float(input('请输入您的身高(m)：'))
w=float(input('请输入您的体重(kg)：'))
BMI=w/(h**2)
if BMI<=18.4:
    print('偏瘦')
elif BMI>=18.5 and BMI<=23.9:
    print('正常')
elif BMI>=24 and BMI<=27.9:
    print('过重')
elif BMI >= 28:
    print('肥胖')
else:
    print('您输入的内容有误，请重新输入')
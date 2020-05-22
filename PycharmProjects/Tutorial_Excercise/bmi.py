height = float(input('身長をm単位で入力して下さい'))
weight = int(input('体重をkg単位で入力して下さい'))

bmi = weight / height **2
print(bmi)
if bmi < 18.5:
    print('瘦せ型')
elif bmi >= 18.5 and bmi < 25:
    print('普通')
else:
    print('肥満体')
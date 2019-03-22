height = input('請輸入您的身高(m): ')
height = float(height)

weight = input('請輸入您的體重(kg): ')
weight = float(weight)

bmi = weight / (height * height)

if bmi < 18.5:
	fat = str(' ,體重過輕')
	print('您的BMI值為: ', bmi, fat)
elif 18.5 <= bmi < 24:
	fat = str(' ,屬於正常範圍')
	print('您的BMI值為: ', bmi, fat)
elif 24 <= bmi < 27:
	fat = str(' ,過重')
	print('您的BMI值為: ', bmi, fat)
elif 27 <= bmi < 30:
	fat = str(' ,輕度肥胖')
	print('您的BMI值為: ', bmi, fat)
elif 30 <= bmi < 35:
	fat = str(' ,屬於中度肥胖')
	print('您的BMI值為: ', bmi, fat)
else:
	fat = str(' ,屬於重度肥胖')
	print('您的BMI值為: ', bmi, fat)


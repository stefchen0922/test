#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功"
#如果不正確 就印出 "密碼錯誤! 還有___次機會!"

password = 'a123456'
icount = 3

while True:
	if password != input("請輸入密碼:"):
		icount -= 1		
		if icount == 0:
			break
		print("密碼錯誤! 還有" + str(icount) + "次機會")		
	else:
		print("登入成功")
		break

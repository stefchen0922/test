# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

start = input("請決定隨機數字範圍開始值：")
end = input("請決定隨機數字範圍結束值：")

ans = random.randint(int(start), int(end))
count = 0
while True:
	count += 1
	guess = input("請輸入數字: ")
	if int(guess) != ans:
		if int(guess) > ans:
			print("比答案大")
		elif int(guess) < ans:
			print("比答案小")
		print("這是你猜的第", count, "次")
	else:
		print("終於猜對了!")
		print("這是你猜的第", count, "次")
		break

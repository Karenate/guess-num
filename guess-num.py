# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對 印出 "終於猜對了!"
# 猜錯 印出 比答案 大/小

import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count +1 快寫法 
    num = input('數字1~100,請猜數字: ')
    num = int(num) # 字串轉換成整數
    if num == r:
    	print('恭喜猜對了!')
    	print('這是你猜的第', count, '次')
    	break
    elif num > r:
    	print(num, '比答案', r,'大')
    elif num < r:
    	print(num, '比答案', r,'小')
    print('這是你猜的第', count, '次')
# 產生一個隨機整數1~100 (basic version)
# 讓使用者重複輸入數字去猜
# 猜對 印出 "猜對了!"
# 猜錯 印出 比答案 大/小
# 讓使用者決定隨機數字範圍

import random
start = input('請決定隨機數字範圍開始值: ' )
end = input('請決定隨機數字範圍結束值: ' )
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count +1 快寫法 
    num = input('請猜數字: ')
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
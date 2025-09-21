year_input = input("请输入一个年份: ")
try:
    year = int(year_input)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("是闰年")
    else:
        print("不是闰年")
except ValueError:
    print("输入错误: 请输入有效的年份数字")

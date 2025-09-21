# 在此处编写代码
try:
    year_input = input("请输入年份：")
    if year_input.isdigit():
        year = int(year_input)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, "是闰年")
        else:
            print(year, "不是闰年")
    else:
        print("输入年份含有非数字")
except ValueError:
    print("输入年份错误")

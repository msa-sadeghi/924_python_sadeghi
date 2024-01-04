# all_months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# month_number = int(input("enter a number between (1-12): "))

# months = []
# for i in range(len(all_months)//3):
#     months.append(all_months[i*3:(i+1)*3])

# print(months)
# print("your selection is :", months[month_number - 1])

def add_even(n1, n2, n3):
    total = 0
    if n1 % 2 == 0:
        total += n1
    if n2 % 2 == 0:
        total += n2
    if n3 % 2 == 0:
        total += n3
    return total
print(add_even(2,2,4))

"""
یک تابع تعریف کنید که نام و نام خانوداگی و سن فردی را دریافت کند
اگر سنش از 18 بیشتر بود
متن زیر را برگرداند
reza sabouri is 18 years old

"""

"""
یک تابع بنویسید که عددی را دریافت نماید
اگر عدد زوج بود True
و اگر فرد بود
False
را برگرداند

"""
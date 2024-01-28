import datetime

# today = datetime.date.today()
# print(today)
# custom_time = datetime.date(2024,1,10)
# print(custom_time)
# print(custom_time.year)
# print(custom_time.month)
# print(custom_time.day)

# today = datetime.date.today()
# print(f"{today:%m-%d-%Y}")
# t = datetime.time(23, 59, 59, 999999)
# print(t)
# right_now = datetime.datetime.now()
# print(right_now)
#
# date1 = datetime.date(2024, 1, 1)
# date2 = datetime.date(2024, 2, 20)
# d = date2 - date1
# print(d.days)
# date_3 = datetime.date(2024, 1, 18)
# duration = datetime.timedelta(days=150)
# print(date_3 + duration)
# print(date_3 - duration)

# TODO برنامه ای بنویسید که تاریخ تولد فردی را از ورودی دریافت نماید و اختلاف تاریخ تولدش از اکنون را به او نمایش دهد
age = 14
if age >= 18:
    print("adult")
else:
    print("other")
# Ternary operator
age = 14
message = "adult" if age >= 18 else "other"
print(message)

answers = ["A", "B", "", "D"]
# TODO   برنامه ای بنویسید که بررسی کند آیا لیست بالا ناقص است یا خیر
# منظور از ناقص، وجود داشتن متن خالی در لیست می باشد

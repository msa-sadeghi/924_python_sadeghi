# import string
# my_string = "ali0123tyuimnshsjk092345"
# تعداد اعداد موجود در رشته بالا
# مجموع اعداد موجود در شته بالا
# count = 0
# total = 0

# for char in my_string:
#     if char.isdecimal():
#         count += 1
#         total += int(char)

# print("count is:", count)
# print("total is:", total)





# count = 0
# total = 0

# for char in my_string:
    
#     # if char in ('0', '1','2','3','4','5','6','7','8','9'):
#     if char in string.digits:
#         count += 1
#         total += int(char)

# print("count is :", count)
# print("total is :", total)





# s1 = "Hello Every body"
# s2 = "   a b c   "
# s3 = "ABC"
# s4 = "tada."
# print(s3.capitalize())
# print(s1.capitalize())
# print(s2.capitalize())
# print(s1.count(" "))
# print(s4.find("."))
# print(s4.find("y"))
# print(s1.islower())
# print(s3.lower())
# print(s2.lstrip())
# print(s2.strip())
# print(s1.swapcase())
# print(s1.title())
# print(s4.upper())

import datetime
today = datetime.date.today()
print(today)
custom_time = datetime.date(2024,1,10)
print(custom_time)
print(custom_time.year)
print(custom_time.month)
print(custom_time.day)
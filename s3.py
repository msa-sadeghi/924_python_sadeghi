"""
برنامه ای بنویسید که نام کاربر را از ورودی دریافت نماید
و این اسامی را در لیستی اضافه نماید
و تا زمانی که 
exit
را وارد نکرده است این کار ادامه پیدا کند
در پایان لیست را نمایش دهید
"""



# all_name = []

# while True:
#     name = input('enter a name: ')
#     all_name.append(name)
#     if input('Do you want to continue...(y or n)? ') == 'n':
#         break

# print(all_name)





message = "1,2,3,4,5,6,7,8,9"
"""
 با کمک حلقه فور برنامه ای بنویسید  که عددهای موجود در متغیر بالا را با هم جمع نماید و حاصل را
 نمایش دهد.
 اینکار را با استفاده از حلقه وایل انجام دهید.

"""
all_numbers = message.split(",")
# total = 0
# for number in all_numbers:
#     total += int(number)
# print(f'total is {total}')

total = 0
i = 0 
while i < len(all_numbers):
    total += int(all_numbers[i])
    i += 1
print(f'total is {total}')

# total = 0
# for item in message:
#     if item != ",":
#         total += int(item)
# print(f'total is {total}')

all_months = "JanFebMarAprMayJunJulAugSepOctNovDec"
month_number = int(input("enter a number between (1-12): "))
for i in range(3):
    print("Hello")

i = 0
while i < 3:
    print("Hello")
    i += 1

total = 0
while True:
    number = int(input("Enter a number: "))
    total += number
    if input("Do you want to quit (y or n)? ") == "y":
        break
print(f'total is :{total}')


name = "ehsan"
age = 13

message = name + " is " + str(age) + " years old."
message = "%s is %s years old." % (name, age)
message = f"{name} is {age} years old."
print(message)

"""
برنامه ای بنویسید که نام کاربر را از ورودی دریافت نماید
و این اسامی را در لیستی اضافه نماید
و تا زمانی که 
exit
را وارد نکرده است این کار ادامه پیدا کند
در پایان لیست را نمایش دهید
"""

message = "1,2,3,4,5,6,7,8,9"
"""
 با کمک حلقه فور برنامه ای بنویسید  که عددهای موجود در متغیر بالا را با هم جمع نماید و حاصل را
 نمایش دهد.
 اینکار را با استفاده از حلقه وایل انجام دهید.

"""

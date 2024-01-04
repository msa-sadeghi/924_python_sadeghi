x = [1,2,3,4,5,9]

print(x[0], x[-1])
print(x[:3])
print(x[3:])

# print("sum is: ",sum(x))

# total = 0
# for number in x:
#     total += number
# print("total is:", total)
# TODO   عملیات جمع را با وایل انجام دهید
# print("list length is", len(x))
# TODO  طول لیست را بدون استفاده از تابع لن  بدست آورید
# for number in x:
#     print(number, end=" ")
# print()
# new_number = int(input("enter a number: "))
# x.append(new_number)
# print("x is:", x)
# another_number = int(input("enter a number: "))
# if another_number in x:
#     x.remove(another_number)
# TODO  درصورت وجود نداشتن عدد در داخل لیست پیغام مناسبی به کاربر
# نمایش داده شود و مجددا از کاربر خواسته شود تا عددی که در لیست وجود دارد را وارد نماید
# در صورتی که به جای عدد نوع داده دیگری نیز داده شود، هم همینطور
# print("x is:", x)



numbers = []
odd_total = 0
for n in range(100, 250):
    if n % 3 == 0:
        numbers.append(n)
        if n % 2 != 0:
            odd_total += n

print("numbers: ", numbers)
print()
print()
print()
print("odd_total",odd_total)
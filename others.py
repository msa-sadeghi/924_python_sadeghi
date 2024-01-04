# n = int(input("enter a number: "))
# while n:
#     print("salaam")

# TODO  تک تک ارقام عدد را جدا کنید
# رقم هایی که زوج هستن را با هم جمع کنید

# n = int(input("enter a number: "))
# even_total = 0
# while n:
#     temp = n%10
#     print(temp)
#     if temp % 2 == 0:
#         even_total += temp
#     n //= 10

# print("even total is:", even_total)

# n = input("enter a number: ")

# for digit in n:
#     print(digit)


favorite_sports = {
    "faranak" : "football",
    "kosar":"tennis",
    "iliya":"football"
}


# for key, value in favorite_sports.items():
#     if value == "football":
#         print(key)




print(f"faranak likes {favorite_sports['faranak']}")
name = input("enter a name: ")
food = input("enter food name: ")
favorite_sports[name] = food
# print(favorite_sports)

del favorite_sports["kosar"]

person = {
    'name': "roze",
    "family":"blalalalal",
    "age":"24"
}

# person = ["roze", "blalalalal", "24"]

# def hello(name):
#     print("hello",name)
#     return ""


# print(hello("roze"))
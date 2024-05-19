# def m():
#     for i in range(1,21):
#         if i==20:
#             print("You got it")
# m()

# import random as r
# d=['1','2','3','4','5','6']
# dn=r.randint(0,5)
# print(d[dn])


# #play computer
# ye=int(input(" "))
# if ye>1980 and ye<1994:
#     print("Millienail")
# elif ye>=1994:
#     print("Gen Z")


# num=int(input())
# if num%2==0:
#     print(f"{num} is even")
# elif num%2!=0:
#     print(f"{num} is odd")

# yr=int(input(" "))
# # if yr%4==0:
# #     if yr%100==0:
# #         if yr %400==0:
# #             print("Leap year")
# #         else:
# #             print("Not leap")
# #     else:
# #         print("Leap")
# # else:
# #     print("Not leap")
# if yr%4==0 and yr%100!=0:
#     print("Leap year")
# elif yr %400==0:
#         print("Leap year")
# else:
#     print("Not leap")

t=int(input(" "))
for i in range(1,t+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

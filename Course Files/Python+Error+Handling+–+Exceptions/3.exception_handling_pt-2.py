# ------------------------------------------------------------
# --------------**## Exception Handling Part 2 ##**-----------


# ******------****** Example 10 ->>>> get a ZeroDivisionError
# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except ValueError:
#     print("please enter a valid age")
# else:
#     print("No Errors Here")


# ******------****** Example 11 ->>>> resolving a ZeroDivisionError

# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except ValueError:
#     print("please enter a valid age")
# except ZeroDivisionError:
#     # print("age cannot be zero")
#     print("please enter a valid age")
# else:
#     print("No Errors Here")


# ******------****** Example 12 ->>>> creating a tuple of erros


# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("please enter a valid age")
# except ZeroDivisionError:
#     print("age cannot be zero")
# else:
#     print("No Errors Here")

# ******------****** Example 13


try:
    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("please enter a valid age")
else:
    print("No Errors Here")

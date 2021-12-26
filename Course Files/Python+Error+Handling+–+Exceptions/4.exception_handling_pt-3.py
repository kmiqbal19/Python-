# ------------------------------------------------------------
# --------------**## Exception Handling Part 3 ##**-----------


# ******------****** Example 14 ->>>> try...except...else...finally

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
#     note.close()
# except (ValueError, ZeroDivisionError):
#     print("please enter a valid age")
# else:
#     print("No Exceptions Here")


# Solution 1 -> moving the close() method to the except clause

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("please enter a valid age")
#     note.close()
# else:
#     print("No Exceptions Here")


# Solution 2 -> duplicate the close method to the else clause

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("please enter a valid age")
#     note.close()
# else:
#     print("No Exceptions Here")
#     note.close()


# Solution 3 -> the finally clause

try:
    note = open("someFile.txt")
    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("please enter a valid age")
else:
    print("No Exceptions Here")
finally:
    note.close()

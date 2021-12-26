# ------------------------------------------------------------
# -----------------**## The with Statement ##**---------------


# ******------****** Example 15 ->>>> opening a single file

# __exit__

# try:
#     with open("someFile.txt") as note:
#         print("note opened")

#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid age.")
# except FileNotFoundError:
#     print("oops")
# else:
#     print("No Exceptions Here")


# ******------****** Example 16 ->>>> opening multiple files

try:
    with open("someFile.txt") as note, open("anotherFil.txt") as my_note:
        print("notes opened")

    # age = int(input("Age: "))
    # x = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age.")
except FileNotFoundError:
    print("file was not found")
else:
    print("No Exceptions Here")

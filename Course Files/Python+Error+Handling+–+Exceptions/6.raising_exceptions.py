# ------------------------------------------------------------
# -----------------**## Raising Exceptions ##**---------------


# ******------****** Example 17 ->>>> raising an exception

# def calculate_age(age):
#     if age <= 0:
#         raise ValueError("age cannot be zero or less")

#     return 10 / age

# calculate_age(0)
# calculate_age(-5)


# ******------****** Example 18 ->>>> raising an exception and handling it


def calculate_age(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")

    return 10 / age


try:
    # calculate_age(0)
    # calculate_age(-5)
    calculate_age(15)
except ValueError as error:
    print(error)

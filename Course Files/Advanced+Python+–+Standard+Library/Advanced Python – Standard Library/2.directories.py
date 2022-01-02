# ------------------------------------------------------------
# --------------------**## Directories ##**-------------------
from pathlib import Path

my_directory = Path("real_estate")
new_directory = Path("social")


# -------------------- Useful Directory Methods --------------------

# 1- exists() ->>>> Checking whether or not the directory exisits
# print(my_directory.exists())

# 2- mkdir() ->>>> creating the directory
# my_directory.mkdir()

# 3- rmdir() ->>>> removing the directory
# my_directory.rmdir()


# 4- rename() ->>>> renaming the directory
# my_directory.rename("property_dealer")

# 5- iterdir() ->>>> getting the list of files and directories at this path

# print(new_directory.iterdir())

# Generator Object
# for data in new_directory.iterdir():
#     print(data)


# LC

# social_data = [data for data in new_directory.iterdir()]
# print(social_data)

# 6- is_file() ->>>> Getting only the files
# paths = [data for data in new_directory.iterdir() if data.is_file()]
# print(paths)

# 7- is_dir() ->>>> Getting only the directories
# paths = [data for data in new_directory.iterdir() if data.is_dir()]
# print(paths)

# Case 1: Searching using a pattern using the asterisk symbol (*)
# paths = [data for data in new_directory.iterdir() if data.is_dir()]

# python_files = [data for data in new_directory.glob("*.py")]

# print(paths)
# print(python_files)

# Case 2: Searching recursively using the rglob() method
# python_files = [data for data in new_directory.rglob("*.py")]


python_files = [data for data in new_directory.rglob("*.*")]

print(python_files)

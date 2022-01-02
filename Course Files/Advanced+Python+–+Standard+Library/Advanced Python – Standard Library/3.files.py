# ------------------------------------------------------------
# -----------------------**## Files ##**----------------------


from pathlib import Path

from time import ctime

import shutil


source = Path("property_dealer/property.py")
new_source = Path("property_dealer/app.py")
my_directory = Path("property_dealer/__init__.py")


# --------------------------- Useful Files Methods -------------------------

# 1- exists() ->>>> Checking whether or not the file exists
# print(source.exists())

# 2- rename() ->>>> renaming the file
# source.rename("property_dealer/app.py")

# 3- unlink() ->>>> removing the file
# new_source.unlink()

# 4- stat() ->>>> returns info about the file
# print(my_directory.stat())
# print(ctime(my_directory.stat().st_atime))
# print(ctime(my_directory.stat().st_mtime))
# print(ctime(my_directory.stat().st_ctime))

# The following 4 methods take care of opening and closing files *-*-*-*-*

# 5- read_bytes() ->>>> reading data from a file ->>> returns the content of the file as a bytes object for representing binary data
# print(my_directory.read_bytes())


# 6- read_text() ->>>> reading the content of the file as a string
# print(my_directory.read_text())

# 7- write_bytes() ->>>> writing to a file
# print(my_directory.write_bytes(b'print("Hello From The Sun")'))
# print(my_directory.read_text())

# 8- write_text() ->>>> writing to a file as a string
# print(my_directory.write_text("print('Hello From Venus')"))
# print(my_directory.read_text())

# 9- Copying a file to another location
target_directory = Path("astronomy")

shutil.copy(my_directory, target_directory)

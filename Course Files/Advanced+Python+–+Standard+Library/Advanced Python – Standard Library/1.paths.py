# ------------------------------------------------------------
# -----------------------**## Paths ##**----------------------

# https://docs.python.org/3/library/

from pathlib import Path


# *-*-*-*-*-*-*-*-* creating an absolute path on windows
# path = Path("C:\\Program Files\\Python 3")
# print(path)

# *-*-*-*-*-*-*-*-* Using raw string to simplify the path creation
# path = Path(r"C:\Program Files\Python 3")
# print(path)

# *-*-*-*-*-*-*-*-* relative paths
# path = Path("users/__init__.py")
# print(path)

# *-*-*-*-*-*-*-*-* a Path() object that represents the current folder
# path = Path()

# *-*-*-*-*-*-*-*-* combining Path() objects together
# path_2 = Path("Some_Path") / Path("users")
# print(path_2)

# *-*-*-*-*-*-*-*-* combining a Path() object with a string
# path_3 = Path("some_file") / "ecommerce" / "__init__.py"
# print(path_3)

# *-*-*-*-*-*-*-*-* Getting the home directory of the current user
# print(Path.home())


# *-*-*-*-*-*-*-*----------------------------*-*-*-*-*-*-*-*-*
path = Path("social/audio")
path2 = Path("social/images/__init__.py")
path3 = Path("users")

# *-*-*-*-*-*-*-*-* calling the exists method to find out if this file or directory exists or not

# print(path.exists())
# print(path2.exists())
# print(path3.exists())


# *-*-*-*-*-*-*-*-* to check to see if this path is a file

# print(path.is_file())
# print(path2.is_file())
# print(path3.is_file())

# *-*-*-*-*-*-*-*-* to check to see if this path is a directory

# print(path.is_dir())
# print(path2.is_dir())
# print(path3.is_dir())


# *-*-*-*-*-*-*-*-* extracting individual componenets in this path
# returns the file name in path

# print(path.name)
# print(path2.name)
# print(path3.name)


# *-*-*-*-*-*-*-*-* extracting individual componenets in this path
# returns the file name in path without the extension


# print(path.stem)
# print(path2.stem)
# print(path3.stem)


# *-*-*-*-*-*-*-*-* extracting individual componenets in this path
# returns the file name extension

# print(path.suffix)
# print(path2.suffix)
# print(path3.suffix)


# *-*-*-*-*-*-*-*-* extracting individual componenets in this path
# returns the parent of the file

# print(path.parent)
# print(path2.parent)
# print(path3.parent)


# *-*-*-*-*-*-*-*-* creates a new path with the file name changed

# path3 = path2.with_name("__initial__.txt")
# print(path3)

# *-*-*-*-*-*-*-*-* getting the absolute path for the newly created file
# print(path3.absolute())

# *-*-*-*-*-*-*-*-* changing the extension of a file

# print(path3.with_suffix(".js"))

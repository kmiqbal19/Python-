# ------------------------------------------------------------
# --------------------**## CSV Files ##**---------------------

import csv


# ******************* Task One -----------------------
# *-*-*-*-*-*- Opening a CSV file and inserting simple data in it

with open("users_info/users.csv", "w", newline="") as users_data:
    CSV_writer_data = csv.writer(users_data)

    # row 1 ->>>> table heading
    CSV_writer_data.writerow(["User Name", "User ID", "Status"])

    # row 2 ->>>> first row of user data
    CSV_writer_data.writerow(["cool555", 111, "online"])

    # row 3 ->>>> second row of user data
    CSV_writer_data.writerow(["333awesome", 222, "offline"])

    # row 4 ->>>> third row of user data
    CSV_writer_data.writerow(["dog", 333, "online"])

    # row 5 ->>>> forth row of user data
    CSV_writer_data.writerow(["cat", 444, "online"])


# ******************* Task Two -----------------------
# *-*-*-*-*-*- Reading a CSV file

with open("users_info/users.csv") as users_data:
    CSV_reader_data = csv.reader(users_data)
    # print(list(CSV_reader_data))

    for data_row in CSV_reader_data:
        print(data_row)

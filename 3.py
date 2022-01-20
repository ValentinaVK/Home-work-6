import os
import sys
from itertools import zip_longest


def reader_fail(user_1, hobby_1):
    with open(user_1, "r") as user_2, open(hobby_1, "r") as hobby_2:
        for user, hobby in zip_longest(user_2, hobby_2):
            yield (user.removesuffix("\n"), hobby.removesuffix("\n") if hobby else None)


def groping(output_, user_1, hobby_1):


    if not (os.path.isfile(user_1) or
            os.path.isfile(hobby_1)):
        return -1

    with open(output_, "w") as out_file:
        for line in reader_fail(user_1, hobby_1):
            print(f"{line[0]}: {line[1]}", file=out_file)

    return 0



user_name = ""
hobby_name = ""
output_name = ""

if len(sys.argv[1:]) >= 3:
    user_name = sys.argv[1]
    hobby_name = sys.argv[2]
    output_name = sys.argv[3]

if not user_name:
    user_name = "users.csv"

if not hobby_name:
    hobby_name = "hobby.csv"

if not output_name:
    output_name = "out.txt"

exit(groping(user_1=user_name, hobby_1=hobby_name, output_=output_name))
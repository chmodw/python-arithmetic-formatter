def arithmetic_arranger(problems, answers=False):

    arithmetics = []
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    # breaking down the problems list into sub lists
    for item in problems:
        arithmetics.append(item.split(" "))

    # return error if more than 5 problems present
    if len(arithmetics) > 5:
        return ("Error: Too many problems.")

    # looping the arithmetics list
    for items in arithmetics:
        # making sure numbers has only 4 digits
        for item in items:
            if len(item) > 4:
                return ("Error: Numbers cannot be more than four digits.")

        # convert string to numbers. if can't return an error
        try:
            items[0] = int(items[0])
            items[2] = int(items[2])
        except ValueError:
            return ("Error: Numbers must only contain digits.")

        maxLength = len(str(getMax(items)))
        minLength = len(str(getMin(items)))

        # adding row one

        # adding row two

        # adding row three

        # adding row four

    return (row1[1:] + "\n" + row2 + "\n" + row3 + "\n" + row4)


def getMax(list):
    return max([list[0], list[2]])


def getMin(list):
    return min([list[0], list[2]])


print(arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))


#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474

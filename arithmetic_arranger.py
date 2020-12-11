def arithmetic_arranger(problems, answers=False):

    arithmetics = []

    # breaking down the problems list into sub lists
    for item in problems:
        arithmetics.append(item.split(" "))

    # return error if more than 5 problems present
    if len(arithmetics) > 5:
        return ("Error: Too many problems.")

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

    return arithmetics


print(arithmetic_arranger(
    ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))


#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474

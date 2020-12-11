def arithmetic_arranger(problems, answers=False):

    arithmetics = []

    # breaking down the problems list into sub lists
    for item in problems:
        arithmetics.append(item.split(" "))

    # return error if more than 5 problems present
    if len(arithmetics) > 5:
        return ("Error: Too many problems.")

    # convert string to numbers
    for item in arithmetics:
        try:
            item[0] = int(item[0])
            item[2] = int(item[2])
        except ValueError:
            return ("Error: Numbers must only contain digits.")

    return arithmetics


print(arithmetic_arranger(
    ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))


#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474

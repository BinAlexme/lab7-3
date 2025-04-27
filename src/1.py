def average_num(list_num: list) -> str | float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except TypeError:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)



# assert
assert average_num([0]) == 0
assert average_num([0, 0]) == 0
assert average_num([1, 1, 1]) == 1
assert average_num([2.5, 3.5]) == 3
assert average_num([1, 2, 3]) == 2
assert average_num([1.1, 2.2, 3.3]) == 2.2
assert average_num([-1, -2, -3]) == -2
assert average_num([2, [3, 4, 5], 6, 8]) == "Bad request"
assert average_num([2, "True", 4.8, 8]) == "Bad request"
assert average_num([1, 2, 3, True]) == "Bad request"
assert average_num([1, 2, 6, False]) == "Bad request"
# assert average_num(12) == "Bad request"  TypeError

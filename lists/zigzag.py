# draft for https://leetcode.com/problems/zigzag-conversion/
def convert(s: str, nums_count: int):
    i = 0
    lst = []
    while i < len(s):
        lst.append(list(s[i:i + nums_count]))
        i = i + nums_count - 1

    i, j = 0, 0
    results = []
    # while i < nums_count:
    #     new_str = ""
    #     j = 0
    #     while j < len(lst):
    #         new_str += lst[j][i]
    #         j = j + nums_count - 1
    #     results.append(new_str)
    #     i += 1
    # print(results)

    return lst


if __name__ == "__main__":
    print(convert("ABCDEHMNLO", 3))




import collections


def compress_string(input):
    arr = []
    my_index = 0
    for index, element in enumerate(input):
        if element in "({":
            if my_index != index:
                arr.append(input[my_index:index])
                my_index = index
        elif element in "})":
            arr.append(input[my_index:index + 1])
            my_index = index + 1
        elif index == len(input) - 1:
            arr.append(input[my_index:])

    print(arr)

    transformed_string = ""
    for i in range(len(arr)):
        if i + 1 < len(arr) and "(" in arr[i] and "{" in arr[i + 1]:
            transformed_string += arr[i][1:-1] * int(arr[i + 1][1:-1])
        elif "{" not in arr[i]:
            transformed_string += arr[i]
    return transformed_string


print(compress_string('ab(c){7}(d){2}'))


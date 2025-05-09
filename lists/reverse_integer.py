
# https://leetcode.com/problems/reverse-integer/
def reverse(x: int) -> int:
    s = 0

    sign = -1 if x < 0 else 1
    x = abs(x)
    while x:
        s = s * 10 + x % 10
        x = x // 10

    return (sign * s) if s < 2**31 else 0



if __name__ == "__main__":
    print(reverse(1534236469))
                
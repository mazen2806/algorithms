def longest_palindrome_v1(s: str) -> str:
    palindrome = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = s[i:j + 1]
            if sub_str == sub_str[::-1]:
                if len(sub_str) > len(palindrome):
                    palindrome = sub_str

    return palindrome

# faster solution
def longest_palindrome_v2(s: str) -> str:
    # input s: string
    # output string
    s_len = len(s)
    result = ''
    def get_palindrome(l, r):
        # return palindrome string
        while l >= 0 and r < s_len and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    for i in range(s_len):
        len1 = len(get_palindrome(i, i))
        len2 = len(get_palindrome(i, i + 1))

        if len1 > len(result):
            result = get_palindrome(i, i)

        if len2 > len(result):
            result = get_palindrome(i, i + 1)
    return result

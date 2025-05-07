# Leet code issue: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s: str) -> int:
    long_substr = {}

    if not s:
        return 0

    for i in range(len(s)):
        sub_s = s[i]
        long_substr[sub_s] = len(sub_s)

        for j in range(i+1, len(s)):
            if s[j] not in sub_s:
                sub_s += s[j]
                long_substr[sub_s] = len(sub_s)
            else:
                break

    v = list(long_substr.values())
    return max(v)


# The fast solution
class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        lis = []
        res = len(lis)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in lis:
                    lis.append(s[j])
                    res = max(res, len(lis))
                else:
                    res = max(res, len(lis))
                    lis = []
                    break
        return res


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("pwwkew"))
    print(length_of_longest_substring("bbbbbbbb"))
    print(length_of_longest_substring(""))

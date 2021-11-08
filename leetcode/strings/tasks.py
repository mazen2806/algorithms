from typing import List


def reverseString(s: List[str], indx=0) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) < 2 or indx >= len(s) / 2:
        return

    s[indx], s[-1 - indx] = s[-1 - indx], s[indx]

    reverseString(s, indx + 1)


def isAnagram(s: str, t: str) -> bool:
    dict1 = {}
    dict2 = {}

    for i in s:
        dict1[i] = dict1.get(i, 0) + 1

    for i in t:
        dict2[i] = dict2.get(i, 0) + 1

    return dict1 == dict2

# https://leetcode.com/problems/valid-parentheses/

def is_valid(s: str) -> bool:
    dct = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    opened = []
    for s_item in s:
        if s_item in dct.keys():
            opened.append(s_item)
            continue
        if s_item in dct.values():
            if opened:
                r = opened.pop()
                if dct[r] == s_item:
                    continue
                else:
                    return False
            else:
                return False

    if opened:
        return False
    return True


if __name__ == "__main__":
    print(is_valid("(){}}{"))
    print(is_valid("(){}"))
    print(is_valid("]"))

# Task F
def findDoublers(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return True
        seen.add(ch)
    return False


print(findDoublers("hello"))
print(findDoublers("world"))

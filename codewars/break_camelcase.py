def solution(s):
    return "".join(f" {x}" if x.isupper() else x for x in s)
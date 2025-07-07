def solution(pairs):
    return ",".join(f"{key} = {value}" for key, value in pairs.items())
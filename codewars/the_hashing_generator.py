def generate_hashtag(s):
    s = "".join(x.capitalize() for x in s.strip().split())
    if not s or len(s) > 139:
        return False
    return f"#{s}"
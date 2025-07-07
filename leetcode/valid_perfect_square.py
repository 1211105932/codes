class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = num ** 0.5
        return num.is_integer()
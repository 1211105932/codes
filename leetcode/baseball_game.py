class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in operations:
            match i:
                case "+":
                    res.append(res[-2] + res[-1])
                case "D":
                    res.append(res[-1] * 2)
                case "C":
                    res.pop()
                case _:
                    res.append(int(i))

        return sum(res)
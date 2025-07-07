class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][1]:
                stack_i, stack_j = stack.pop()
                res[stack_i] = i - stack_i
            
            stack.append((i, j))
        
        return res
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        m = 0
        for i in reversed(range(len(arr) - 1)):
            m = max(m, arr[i+1])
            ans.append(m)
        return ans[::-1]
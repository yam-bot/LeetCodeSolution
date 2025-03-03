# [2,5,7,11,15]
# [1,2,5,7,11,15]
#  ^ ^
#  ^   ^
# [0,3,3,4,5,6]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0 , len(numbers)-1
        ans = [left,right]
        while (numbers[left] + numbers[right]) != target and left != right:
            if (numbers[left] + numbers[right]) < target:
                left += 1
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
        ans = [left+1, right+1]
        return ans
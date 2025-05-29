from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []


def main():
    test = Solution()
    print(test.twoSum([2, 7, 11, 15], 9))
    print(test.twoSum([3, 2, 4], 6))
    print(test.twoSum([3, 3], 6))


if __name__ == '__main__':
    main()
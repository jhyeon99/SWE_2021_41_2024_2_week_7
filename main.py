from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # 맵에 지나간 숫자와 인덱스를 저장
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        # 맵을 탐색
        if complement in num_map:
            return [num_map[complement], i]  # 두 숫자의 인덱스를 반환
        num_map[num] = i  # 맵에 현재 숫자와 그 인덱스를 저장
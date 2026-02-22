class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in range(len(nums)):
            if nums[i] not in freq_table.keys():
                freq_table[nums[i]] = 1
            else:
                freq_table[nums[i]] += 1
        bucket_array = [[] for i in range(len(nums) + 1)]

        for item, count in freq_table.items():
            bucket_array[count].append(item)

        res = []
        for i in range(len(bucket_array) - 1, 0, -1):
            for num in bucket_array[i]:
                res.append(num)
                if len(res) == k:
                    return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)
        
        for n, c in count_map.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
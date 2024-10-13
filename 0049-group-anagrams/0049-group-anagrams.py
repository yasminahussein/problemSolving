class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_ang = defaultdict(list)
        for str1 in strs:
            key ="".join(sorted(str1))
            sorted_ang[key].append(str1)
        return sorted_ang.values()
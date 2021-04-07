#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()
        s_count = 0
        t_count = 0

        for sc, tc in zip(s, t):
            if sc not in s_map:
                s_map[sc] = s_count
                s_count += 1
            if tc not in t_map:
                t_map[tc] = t_count
                t_count += 1
            
            if s_map[sc] != t_map[tc]:
                return False
        return True
        
# @lc code=end


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1:
            return False
        diff_idxs = []
        same_dict = {}
        for i in range(len(s)):
            if s[i] == goal[i]:
                same_dict[s[i]] = same_dict.get(s[i], 0) + 1
            else:
                diff_idxs.append(i)
        if len(diff_idxs) == 2:
            if s[diff_idxs[1]] + s[diff_idxs[0]] == goal[diff_idxs[0]] + goal[diff_idxs[1]]:
                return True
        if len(diff_idxs) == 0 and any(map(lambda x: x >= 2, same_dict.values())):
            return True
        return False

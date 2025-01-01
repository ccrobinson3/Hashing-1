############## Check if two strings are isomorphic  ######

# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Using two hashmaps store the mapping from s to t and t to s. If there is a conflict
# in the mapping return False


def isIsomorpic(s,t):
    if len(s)!=len(t):
            return False
    mapper_s = {}
    mapper_t = {}
    for i in range(len(s)):
        if s[i] not in mapper_s:
            mapper_s[s[i]] = t[i]
        else:
            if t[i] != mapper_s[s[i]]:
                return False
        if t[i] not in mapper_t:
            mapper_t[t[i]] = s[i]
        else:
            if s[i] != mapper_t[t[i]]:
                return False
    return True


############## Group Anagrams ######

# Time Complexity : O(n*m)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# For every word get the count of the characters and use that as the hashkey 
# and hash the words based on that and add to hashmap. Then return the values as the 
# grouping

from collections import defaultdict

def group_anagram(strs):
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(word)

    result = []
    for k in groups.keys():
        result.append(groups[k])
    return result
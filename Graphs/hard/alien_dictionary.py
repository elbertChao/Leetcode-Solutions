# Question # 269 in Arrays (graph question)
# Description: my implementation for the solution for the Alien Dictionary problem on leetcode
# Problem: There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
#           You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words`
#           are **sorted lexicographically** by the rules of this new language.
#           If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `"".`
#           Otherwise, return *a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by
#           the new language's rules.* If there are multiple solutions, return ***any of them***.
# Difficulty: hard
# Author: Elbert C.

from typing import List

# TC = O(N + V + E) where N = words * lengths for each word, V = unique chars, E = edges in graph
# SC = O(V + E), since we are storing visited that holds up to all edges and Adj sets that have all unique chars

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        # now go through all pairs of words to create adjacencies between any adjacent characters
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            # going to be used to check if in the min length between these 2 words is there an edge case where w1 is longer
            # or at any letter within the min length is different then add it to adj sets
            min_len = min(len(w1), len(w2)) 
            if w1[:min_len] == w2[:min_len] and w1 > w2: # w1 is in the wrong order, w2 should be above in lexicograph
                return ""
            
            # now we can go through all the characters in the min length of both words to check for differences
            for j in range(min_len):
                if w1[j] != w2[j]: # we found a difference in characters at one of the positions
                    adj[w1[j]].add(w2[j]) # add the adjacent character to the first one's set, this makes our graph
                    break
        
        visited = {} # False means it is visited, True means it is a node in our current path
        ans = []

        def dfs(c):
            if c in visited: # if this returns True then there is loop, False otherwise
                return visited[c]
            
            visited[c] = True
            
            # check each adj neighbor for loops in recursive dfs check
            for neigh in adj[c]:
                if dfs(neigh):
                    return True

            visited[c] = False
            ans.append(c)

        for c in adj:
            if dfs(c): # if there are any loops that dfs finds, then return empty string since there is smth wrong in the graph, must be DAG (directed acyclic grapH)
                return ""
        
        ans.reverse() # reverse the string since we did a DFS, answer would be in reverse order, although ordering doesnt matter
        return "".join(ans)
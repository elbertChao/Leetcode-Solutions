# Question # 127 in Arrays (graph question)
# Description: my implementation for the solution for the Word Ladder problem on leetcode
# Problem: A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#           Every adjacent pair of words differs by a single letter.
#           very si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#           sk == endWord
#           Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if 
#           no such sequence exists.
# Difficulty: hard
# Author: Elbert C.

import collections
from typing import List

# TC = O(n*m^2) since there are n words to go through and m operation to get a pattern and then another m for the list of patterns that m has
# SC = O(n*m^2) since we have to go through all the words adding it to our visited set
#      then we are saving the pattern for each word m and their patterns up to length of m

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # if we add a new key to our neighbors dictionary it'll initialize it with empty list
        neigh = collections.defaultdict(list)
        wordList.append(beginWord)

        # create our adjacency dict
        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + "*" + word[c + 1:]
                neigh[pattern].append(word)
        
        # now we can start our BFS
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        ans = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                # check if the word we just popped is the word we are looking for
                if word == endWord:
                    return ans

                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c + 1:]
                    # now we can find all the neighbor words to this word with same patterns
                    # aka all the 1 letter adjacent words
                    for neigh_word in neigh[pattern]:
                        if neigh_word not in visited:
                            visited.add(neigh_word)
                            queue.append(neigh_word)

            ans += 1
        
        # no path or adjacent words found
        return 0

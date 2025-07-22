# Question # 207 in Arrays
# Description: my implementation for the solution for the Course Schedule problem on leetcode
# Problem: There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#           You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#           For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#           Return true if you can finish all courses. Otherwise, return false.
# Difficulty: medium
# Author: Elbert C.

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use a prereq map that maps each course to their prereqs
        pre_map = {i:[] for i in range(numCourses)}

        # populate each course with its prereqs
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # use a visited set to keep track of duplicate courses in DFS path
        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if pre_map[course] == []:
                return True # wasn't already visited and prereq's aren't cleared yet

            visited.add(course)
            # explore all the prereqs
            for prereq in pre_map[course]:
                if not dfs(prereq): # that prereq is already visited so loop occurred
                    return False # can't be fulfilled
            
            # done exploring, we can remove this course from our visited list
            visited.remove(course)
            pre_map[course] = [] # next time this course is searched it will be O(1) operation
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
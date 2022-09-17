from collections import defaultdict
from typing import Dict, List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

        If the town judge exists, then:

        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

        Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

        Workflow

        1. Find the vertex with the greatest indegree
        2. See if that greatest indegree is equal to n - 1 
        4. See if that vertex has an outdegree of 0 (no outdegree at all)
        3. See if this case only happens for once
        """
        indegree_longest_length, longest_indegree_vertex = 0, 1
        outdegree_count_map: Dict[int, int] = defaultdict(int)
        indegree_map: Dict[int, List[int]] = defaultdict(list)
        for t in trust:
            truster, trustee = t
            # outdegree of A to B means A trusts B
            outdegree_count_map[truster] += 1
            # indegree of A to B means B trusts A (A is trusted by B) 
            indegree_map[trustee].append(truster)
            # longest length of indegree must be the town judge, if it exists. 
            if indegree_longest_length < len(indegree_map[trustee]):
                longest_indegree_vertex = trustee
                indegree_longest_length = len(indegree_map[trustee])
            # if there are multiple indegrees of the same length, the town judge does not exist
            elif indegree_longest_length == len(indegree_map[trustee]):
                longest_indegree_vertex = -1
                indegree_longest_length = indegree_longest_length
        # return the only greatest indegree of a vertex that is equal to n - 1 and has no outdegree at all
        return longest_indegree_vertex if indegree_longest_length == n - 1 and longest_indegree_vertex not in outdegree_count_map else -1
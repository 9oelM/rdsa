# https://programmers.co.kr/learn/courses/30/lessons/43162

def findPath(startNode, graph):
    visited = []
    stack = []
    stack.append(startNode)
    while stack:
        # get one of the connections from this node
        node = stack.pop()
        # if not visited yet, visit. 
        if node not in visited:
            visited.append(node)
            # then, move to the visited node and start over
            stack += graph[node]
    return visited

def solution(n : int, computers : List[List[int]]) -> int:
    """
    1. make a dictionary with keys specifying the node number and values specifying the list of the node numbers it's connected to
    2. traverse from each node to check path
    3. unique paths 
    """
    nodes = {idx: [] for idx in range(n)}
    for idx, computer in enumerate(computers):
        for idx2, node in enumerate(computer):
            if node == 1 and idx != idx2:
                nodes[idx2].append(idx)
    paths = []
    for key in nodes:
        paths += [searchPath(key, nodes)]
    paths = [sorted(path) for path in paths]
    paths = list({tuple(path) for path in paths})
    
    return len(paths)

testCases = [(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])]

for n, computers in testCases:
    print(solution(n, computers))

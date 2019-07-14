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


def solution(n, computers):    
    nodes = {idx : [] for idx in range(n)}
    for i, computer in enumerate(computers):
        for idx, elem in enumerate(computer):
            if elem == 1 and i != idx:
                nodes[i].append(idx)

    paths = []    
    for node in nodes:
        paths += [findPath(node, nodes)]
    paths = [sorted(path) for path in paths]
    # unique paths
    paths = list({tuple(path) for path in paths})
    return len(paths)

testCases = [(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])]

for n, computers in testCases:
    print(solution(n, computers))
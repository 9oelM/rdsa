// https://leetcode.com/problems/find-if-path-exists-in-graph/
/**
 * using stack makes it possible to keep the DFS going, because
 * top() and pop() always refer to the last visited element, which is what DFS is about
 */
function validPath(_n: number, edges: number[][], source: number, destination: number): boolean {
  const graph: Record<number, number[]> = {}
  for (const edge of edges) {
    if (edge[0] in graph) graph[edge[0]].push(edge[1])
    else graph[edge[0]] = [edge[1]]
    if (edge[1] in graph) graph[edge[1]].push(edge[0])
    else graph[edge[1]] = [edge[0]]
  }

  const stack: number[] = [source]
  const visited: Set<number> = new Set()

  while (stack.length) {
    const top: number | undefined = stack[stack.length - 1]

    if (top === destination) {
      return true;
    }
    stack.pop()
    if (top === undefined) break
    for (const node of graph[top]) {
      if (!visited.has(node)) {
        visited.add(node)
        stack.push(node)
      }
    }
  }

  return false
};
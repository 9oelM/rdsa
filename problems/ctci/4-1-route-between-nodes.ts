// https://leetcode.com/problems/find-if-path-exists-in-graph/

type Nodes = Record<number, { adjacent: number[], visited?: boolean }>

function dfs(nodes: Nodes, source: number, destination: number) {
  const root: Nodes[number] | undefined = nodes[source]
  
  if (!root) return false
  
  if (source === destination) return
  for (const nodeId of root.adjacent) {
    const n: Nodes[number] | undefined = nodes[nodeId] 

    if (n && !n.visited) {
      dfs(nodes, nodeId, destination)
    }
  }
}

function storeEdge(edge: number[], nodes: Nodes, sourceNodeIndex: 0 | 1 = 0) {
  const targetNodeId = sourceNodeIndex === 0 ? 1 : 0 
  if (edge[sourceNodeIndex] in nodes) {
    nodes[edge[sourceNodeIndex]].adjacent.push(edge[targetNodeId])
  } else {
    nodes[edge[sourceNodeIndex]] = {
      adjacent: [edge[targetNodeId]],
    }
  }
}

function validPath(_n: number, edges: number[][], source: number, destination: number): boolean {
  const nodes: Nodes = {}
  for (const edge of edges) {
    storeEdge(edge, nodes, 0)
    storeEdge(edge, nodes, 1)
  }
  dfs(nodes, source, destination)
  
  return !!nodes[destination]?.visited
};
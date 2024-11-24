from collections import defaultdict, deque

def is_dag(nodes, edges):
    if(nodes.length < 2): 
        return True

    # Create adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    visited_nodes = set()
    
    # Initialize graph structure
    for edge in edges:
        source, target = edge['source'], edge['target']
        source, target = edge['source'], edge['target']
        adj_list[source].append(target)
        in_degree[target] += 1
        in_degree[source] += 0  # Ensure source has an entry even if it has no incoming edges
        visited_nodes.add(source)
        visited_nodes.add(target)
    
    # Check if the graph includes all given nodes
    if set(nodes) != visited_nodes:
        return False
    
    # Topological Sort using Kahn's Algorithm
    zero_in_degree = deque([node for node in nodes if in_degree[node] == 0])
    sorted_nodes = []

    while zero_in_degree:
        current = zero_in_degree.popleft()
        sorted_nodes.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # If all nodes are not visited, the graph has a cycle
    return len(sorted_nodes) == len(nodes)


# nodes = ["A", "B", "C", "D"]
# edges = [{"source": "A", "target": "B"}, {"source": "B", "target": "C"}, {"source": "C", "target": "D"}]

# print(is_dag(nodes, edges))  # Output: True

# nodes = ["A", "B", "C"]
# edges = [{"source": "A", "target": "B"}, {"source": "B", "target": "C"}, {"source": "C", "target": "A"}]

# print(is_dag(nodes, edges))  # Output: False (contains a cycle)

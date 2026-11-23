class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]  
        size = [1] * (len(edges) + 1)

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False
            
            if size[parent1] > size[parent2]:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            else:
                parent[parent1] = parent2
                size[parent2] += size[parent1]

            return True
    
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
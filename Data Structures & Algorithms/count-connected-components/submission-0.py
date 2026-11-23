class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        city_size = [1] * n

        def find(node):
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0
            
            if city_size[parent1] > city_size[parent2]:
                parent[parent2] = parent1
                city_size[parent1] += city_size[parent2]
            else:
                parent[parent1] = parent2
                city_size[parent2] += city_size[parent1]
            
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
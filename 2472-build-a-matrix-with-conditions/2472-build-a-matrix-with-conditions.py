class Solution:

    def __topological_sort(self, conditions: List[int], k: int) -> List[int]:
        """
        Performs Topological Sorting To Determine Ordering Of Rows And Columns

        T.C = O(V + E)
        S.C = O(V + E)
        """

        """
        Topological sorting is used for ordering the vertices of a directed acyclic graph (dag) in a linear sequence,
        such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

        1. Row conditions:
            Treat each condition [above(i), below(i)] as a directed edge above(i) -> below(i).
            The topological sort will provide an ordering where each above(i) appears before below(i).
            This ensures that above(i) is placed in a row above below(i).

        2. Column conditions:
            Treat each condition [left(i), right(i)] as a directed edge left(i) -> right(i).
            The topological sort will provide an ordering where each left(i) appears before right(i).
            This ensures that left(i) is placed in a column to the left of right(i).
        """

        # Final ordering
        order: List[int] = []
        # Incoming edges for each node (K + 1, Because of 1 based indexing)
        in_degree: List[int] = [0] * (k + 1)
        # Creating graph for given Row/Column conditions
        graph: DefaultDict[List[int]] = defaultdict(list)

        for u, v in conditions:

            # Building graph
            graph[u].append(v)

            # Updating in degree.
            in_degree[v] += 1
        
        # We'll start with nodes which has 0 incoming edges.(These can be placed first in Topological Order)
        queue: Deque = deque([num for num in range(1, k + 1) if in_degree[num] == 0])

        while queue:

            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:

                in_degree[neighbor] -= 1

                # If Neighbor `in_degree` becomes 0, Add it in queue.
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If Topological Sort contains all `k` Nodes, return `order` List else `[]`
        return order if len(order) == k else []

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        T.C = O(K * K)
        S.C = O(K * K)
        """

        row_order: List[int] = self.__topological_sort(rowConditions, k)
        column_order: List[int] = self.__topological_sort(colConditions, k)

        if not row_order or not column_order:
            return []
        
        # Init. a `k` * `k` matrix
        matrix: List[List[int]] = [[0] * k for _ in range(k)]

        # Map containing each Row and Column, and their Values
        row_and_value: Dict[int, int] = {value: row for row, value in enumerate(row_order)}
        column_and_value: Dict[int, int] = {value: col for col, value in enumerate(column_order)}

        # Each number in [1, K], Find it's position and value for the matrix
        for value in range(1, k + 1):
            row: int = row_and_value[value]
            column: int = column_and_value[value]

            matrix[row][column] = value
        
        return matrix
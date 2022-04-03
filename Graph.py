class BaseGraph:

    """
    Directed graph support as adjacency list

    A --> B --> C
    |
    |
    v
    D --> E
    |     ^
    |     |
    v     |
    F ----

    graph = {"A":["B", "D"],
             "B": ["C"],
             "C": [],
             "D": ["E", "F"],
             "E": [],
             "F": ["E"]
             }
    """


    def compute(self, *args, **kwargs):
        pass

    def depth_first_loop(self, graph, source):
        """
        * Implements depth first traverse with loop.
        * First depth method move forwards as much as possible until finds
        a dead end.
        * The logic uses a stack
        * Perform a custom action over each node

        Args:
            graph: Graph to traverse
            source: node from which to traverse from

        Returns:

        """
        stack = [source]
        while (len(stack)) > 0:
            current = stack.pop()
            # performs actions with current node
            self.compute(current)
            for i, neighbor in enumerate(graph[current]):
                stack.append(neighbor)

    def depth_first_recursive(self, graph, source):
        """
        * Implements depth first traverse with recursion.
        * First depth method move forwards as much as possible until finds
        a dead end.
        * The logic uses a stack, that is why is possible to implement with recursion
        which is stack based
        * Perform a custom action over each node

        Args:
            graph: graph to traverse
            source: node from which to traverse from

        Returns:

        """
        # perform actions with current node
        self.compute(source)
        for i, neighbor in enumerate(graph[source]):
            self.depth_first_recursive(graph, neighbor)


    def breath_first(self, graph, source):
        queue = [source]
        while len(queue) > 0:
            current = queue.pop(0)
            # perform a custom action with node
            self.compute(current)
            for i, neighbor in enumerate(graph[current]):
                queue.append(neighbor)

    def has_path_rec(self, graph, src, dst):
        if src == dst:
            return True

        for i, neighbor in enumerate(graph[src]):
            if self.has_path_rec(graph, neighbor, dst):
                return True
        return False

    def has_path_loop(self, graph, src, dst):
        queue = [src]
        while (len(queue)>0):
            current = queue.pop(0)
            if current == dst:
                return True
            for i, neighbor in enumerate(graph[current]):
                queue.append(neighbor)

        return False







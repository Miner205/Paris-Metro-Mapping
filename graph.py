

class Graph:
    def __init__(self, x: str):
        self.nb_vertices: int = 0
        self.nb_arcs: int = 0
        self.list_arcs: list[tuple[int, int, int]] = list()
        self.load_graph_x(x)
        self.adjacency_matrix: list[list] = [['_' for _ in range(self.nb_vertices)] for _ in range(self.nb_vertices)]
        self.compute_adjacency_matrix()
        self.floyd_warshall_graph = []

    def __str__(self):
        return ("Graph details:\n" +
                "Nb of vertices: " + str(self.nb_vertices) + '\n' +
                "Nb of arcs: " + str(self.nb_arcs) + '\n' +
                "All arcs: " + str([arc for arc in self.list_arcs]))

    def load_graph_x(self, x: str) -> None:
        with open("./data/" + x + ".txt", 'r') as f:
            line = f.readline()
            self.nb_vertices = int(line.strip('\n'))
            line = f.readline()
            self.nb_arcs = int(line.strip('\n'))
            for i in range(self.nb_arcs):
                line = f.readline()
                l_temp = line.strip('\n').split(' ')
                self.list_arcs.append((int(l_temp[0]), int(l_temp[1]), int(l_temp[2])))

    def save_graph_as_x(self, x: str) -> None:
        with open("./data/" + x + ".txt", 'w') as f:
            f.write(str(self.nb_vertices) + '\n')
            f.write(str(self.nb_arcs) + '\n')
            for arc in self.list_arcs:
                f.write(str(arc[0]) + ' ' + str(arc[1]) + ' ' + str(arc[2]) + '\n')

    def compute_adjacency_matrix(self) -> None:
        for arc in self.list_arcs:
            self.adjacency_matrix[arc[0]][arc[1]] = arc[2]

    def reverse_adjacency_matrix(self) -> None:
        temp = []
        for i in range(0, len(self.adjacency_matrix)):
            for j in range(0, len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j] != "_":
                    temp.append((i, j, self.adjacency_matrix[i][j]))
        self.list_arcs = temp
        self.nb_arcs = len(temp)

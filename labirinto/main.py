from Maze_graph import Graph, Node


class Maze:

    def __init__(self, file: object, graph) -> object:
        self.file = file
        self.graph = graph
        self.maze = []
        self.number_of_column = 0
        self.line = 0

    def read_file(self) -> Node:
        print('Lendo o arquivo')
        f = open(self.file, "r")

        for row in f:
            self.maze.append(row)
            start = row[0:1]
            if start == 's':
                self.number_of_column = len(row)
                start_line = self.line
                start_node = Node(start_line, 0, 's')
            else:
                self.line += 1

        return start_node

    def wall(self, line, col):
        # é uma parede
        mazeLine = self.maze[line]
        element = mazeLine[col]
        return element == "#"

    def can_goto_wright(self,current):
        # pode ir para direita (linha + 1)
        # fazer a lógica
        if ! wall(self, ...):

        return False

    def find_next(self, current):
        # pode ir para frente (coluna + 1)
        # pode ir para esquerda (linha - 1)
        # pode ir para traz (coluna -1)


    def walk(self, current: Node):
        next = self.find_next(current)
        return next[0], next[1], value

    def next_node(self, current: Node):
        position = self.walk(current)
        next_node = Node(position[0], position[1], position[2])
        return next_node

    def solve(self):
        start_node = self.read_file
        next_node = self.next_node(start_node)
        print('start')
        print(start_node.line)
        print(start_node.column)
        print(start_node.value)
        print('next')
        print(next_node.line)
        print(next_node.column)
        print(next_node.value)

        self.graph.add_edge(start_node,next_node,1)


if __name__ == '__main__':
    problem = Maze('C:\\Users\\ezio.freire\\PycharmProjects\\labirinto\\maze.txt', Graph(1))
    problem.solve()

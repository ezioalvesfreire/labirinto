# Tamanho do labirinto
N = 9

def mostrarSolucao( sol ):

	for i in sol:
		for j in i:
			print(str(j) + " ", end="")
		print("")

def movimentoValido(maze, x, y):

	print(x, y)

	if x >= 0 and x < 29 and y >= 0 and y < 9 and maze[x][y] == '.':
		return True

	return False

def resolverLabirinto( maze ):

	sol = [ [ 'X' for j in range(29) ] for i in range(9) ]

	if resolveLabirintoRecursivo(maze, 3, 0, sol) == False:
		print("nao existe solucao")
		return False

	mostrarSolucao(sol)
	return True

def resolveLabirintoRecursivo(maze, x, y, sol):

	if x == 'f':
		sol[x][y] = 'S'
		return True

	if movimentoValido(maze, x, y) == True:
		sol[x][y] = 'S'

		if resolveLabirintoRecursivo(maze, x + 1, y, sol) == True:
			return True

		if resolveLabirintoRecursivo(maze, x, y + 1, sol) == True:
			return True

		sol[x][y] = 'X'
		return False

def read_file(filename):
    f = open(filename, "r")
    maze = []

    for row in f:
        maze.append(list(row.replace('\n', '')))

    return maze

if __name__ == "__main__":
    maze = read_file('maze.txt')
    resolverLabirinto(maze)
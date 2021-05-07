from functools import reduce

def build_map(file_name, horizontal):
    """
    Purpose:
        Build the hill with trees (#) required by the challenge
    Precond:
        :param file_name: name of .txt file
        :param horizontal: The number of horizontal increments for the provided map
    Return:
        Returns an arrayed list where each item is a horizontal strip of the map
    """
    in_file = open(file_name, "r")
    final_map = []
    for line in in_file:
        new_line = ""
        for n in range(horizontal):
            new_line += line.strip()
        final_map.append(new_line)

    return final_map
    
def challenge_1(tree_map, y_move, x_move):
    """
    Purpose:
        Process a map variable and count the number of times you hit a tree (#) when moving y=1 and x=3 
    Pre:
        :param tree_map: Arrayed list where each list is a horizontal row of the map
        :param y_move: y-movement in the map each step
        :param x_move: x-position in the map each step
    Return:
        Number of times a tree is hit.
    """
    x, y = 0, 0
    tree_hits = 0
    while y < len(tree_map):
        if tree_map[y][x] == "#":
            tree_hits += 1
        y += y_move
        x += x_move
    return tree_hits

def challenge_2():
    """
    Purpose:
        Calculates the product of the number of trees hit for 5 different directional patterns provided by the advent challenge
    Return:
        The product of all the trees hit for 5 different movement patterns
    """
    answers = []
    x_moves = [1, 3, 5, 7, 1]
    y_moves = [1, 1, 1, 1, 2]
    for n in range(len(x_moves)):
        answers.append(challenge_1(build_map("d3/day3_input.txt", 100), y_moves[n], x_moves[n]))
    return reduce(lambda x, y: x*y, answers)


if __name__ == '__main__':
    print(challenge_1(build_map("d3/day3_example.txt", 15), 1, 3))
    print(challenge_1(build_map("d3/day3_input.txt", 35), 1, 3))
    print(challenge_2())

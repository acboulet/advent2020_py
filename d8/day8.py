def process(file_name):
    """
    Purpose:
        Take a .txt file and process so that it returns a list containing all directions
    Pre:
        :param file_name: Name of .txt file
    Return:
        List where each item is a set of directions for the program. Includes a boolean if step is visited
    """
    in_file = open(file_name, "r")
    directions = []
    for line in in_file:
        values = line.strip().split()
        values[1] = int(values[1])
        values.append(False)
        directions.append(values)
    return directions

def infinite_tracker(directions):
    """
    Purpose:
        Executes the directions provided, and returns the value in the accumulator when it
        begins an infitite cycle.
    Pre:
        :param directions: List where each item is a set of directions for the program. Includes a boolean if step is visited
    Return:
        Integer in the accumulator when infinite cycle starts
    """
    accumulator = 0
    current_step = 0
    step = directions[current_step]
    while (not step[2]):       
        if step[0] == "acc":
            accumulator += step[1]
            current_step += 1
        elif step[0] == "jmp":
            current_step += step[1]
        elif step[0] == "nop":
            current_step += 1
        step[2] = True
        step = directions[current_step]
    return accumulator

def program_movement(directions):
    repaired = False
    accumulator = 0
    current_step = 0
    step = directions[current_step]
    # While the spot has not been visited, and not repaired
    while (not step[2] and not repaired):        
        if step[0] == "acc":
            accumulator += step[1]
            current_step += 1
        elif step[0] == "jmp":
            current_step += step[1]
        elif step[0] == "nop":
            current_step += 1
        step[2] = True
        if current_step == len(directions): # Meaning that we have stepped outside of the list
            repaired = True
        else:
            step = directions[current_step]
        
    # if not repaired, and has found an infinite loop then return 0 as a failure
    if step[2] and not repaired:
        return 0
    else:
        return accumulator

def program_repair(directions):
    # Try to change each step in the list of directions until you get one that doesn't end in an inifinite loop
    for n in range(0,len(directions)):
        # Create a new copy of the directions, and modify the current step
        direction_copy = process("d8/day8_input.txt")
        if direction_copy[n][0] == "jmp":
            direction_copy[n][0] = "nop"
        elif direction_copy[n][0] == "nop":
            direction_copy[n][0] = "jmp"
        result = program_movement(direction_copy)
        if result > 0:
            return result

def challenge_1(directions):
    print(infinite_tracker(directions))

def challenge_2(directions):
    print(program_repair(directions))

if __name__ == "__main__":
    directions = process("d8/day8_example.txt")
    challenge_1(directions)
    challenge_2(process("d8/day8_input.txt"))
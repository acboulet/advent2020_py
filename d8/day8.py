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

def program_repair(directions):
    accumulator = 0
    current_step = 0
    step = directions[current_step]
    while (current_step < len(directions)):
        repaired = False
        repaired = try_repair(step)
        def try_repair(step):
            fixed = False
            repaired_step = step.copy()
            if repaired_step[0] == "jmp":
                repaired_step[0] = "nop"
            elif repaired_step[0] == "nop":
                repaired_step[0] = "jmp"

            
            return fixed
        while(not repaired):            
            if step[0] == "acc":
                accumulator += step[1]
                current_step += 1
            elif step[0] == "jmp":
                current_step += step[1]
            elif step[0] == "nop":
                current_step += 1
            step[2] = True
            step = directions[current_step]
        print(step)
    return accumulator

def challenge_1(directions):
    print(infinite_tracker(directions))

def challenge_2(directions):
    print(program_repair(directions))

if __name__ == "__main__":
    directions = process("d8/day8_example.txt")
    challenge_1(directions)
    challenge_2(directions)
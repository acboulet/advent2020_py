def process(file_name):
    """
    Purpose:
        Take a .txt file a process each number on each line.
    Pre:
        :param file_name: Name of a .txt file
    Return:
        List where each item is an integer.
    """
    in_file = open(file_name, "r")
    numbers = []
    for line in in_file:
        numbers.append(int(line.strip()))
    return numbers

def decode_XMAS(cypher):
    """
    Purpose:
        Determines first number value that is not a sum of two numbers in the previous 1-25
    Pre:
        :param cypher: All potential numbers
    Return:
        Integer that does not adhere to cypher code
    """
    # Sets the preconditions
    preamble = 25
    left_c = 0
    right_c = preamble

    # For each number after the first set of options
    for n in cypher[preamble:]:
        # Obtain what the potential options are
        options = cypher[left_c: right_c]
        found = False
        # Try adding each possible number 
        # TODO better to start right from the end
        # if number is found, then just move on
        while not found:
            for left in options:
                for right in options[1:]:
                    total = left + right
                    if total == n:
                        found = True
            if not found:
                return n
        # adjust options selection
        left_c += 1
        right_c += 1
                

if __name__ == "__main__":
    print(process("d9/d9_input.txt"))
    print(decode_XMAS(process("d9/d9_example.txt")))
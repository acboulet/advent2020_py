
from os import name


def process(file_name):
    """
    Purpose:
        Process .txt file to check each unique character in a given group of passengers.
        Groups of passengers are seperated by empty lines.
    Pre:
        :param file_name: name of .txt file
    Return:
        List of unique characters where each group of passengers is a unique string
    """
    in_file = open(file_name, "r")
    all_groups = [] # list of everyone on plane
    group = "" # String consisting of all question characters
    for line in in_file:
        line = line.strip()
        if line == "": # if an empty line, then add the entire group characters and reset for new group
            all_groups.append(group)
            group = ""
        else: # if has group characters, check each one if it is already in group, if not then add to group
            for letter in range(len(line)):
                if not (line[letter] in group):
                    group += line[letter]
    # Add the last group characters to the list because there is no empty line at the end of the .txt
    all_groups.append(group)    
    return all_groups

def challenge_1(group_list):
    """
    Purpose:
        Calculate the sum of total questions where passengers answered 'yes'
    Per:
        :param group_list: List of all unique characters from all groups
    Return:
        Integer of sum total of all counts
    """
    total = 0
    for group in group_list:
        total += len(group)
    return total

if __name__ == "__main__":
    all_groups = process("d6/day6_input.txt")
    
    sum_total = challenge_1(all_groups)
    print(sum_total)

    
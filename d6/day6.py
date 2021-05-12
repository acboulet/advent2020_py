
from os import name


def process_1(file_name):
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

def process_2(file_name):
    in_file = open(file_name, "r")
    all_groups = [] # list of everyone on plane
    group = [] # String consisting of all question characters
    for line in in_file:
        line = line.strip()
        if line == "": # if an empty line, then add the check for common chars and reset group
            all_groups.append(all_answers(group))
            group = []
        else:
            group.append(line)
    all_groups.append(all_answers(group)) # Add last group of chars because no empty line at end
    return all_groups

def all_answers(people_group):
    everyone = {}
    count = 0 # number of people in the group
    for person in people_group:
        count += 1
        for char in person:
            if not (char in everyone): #if not already in dictionary
                everyone[char] = 1
            else:
                everyone[char] += 1
    code = ""
    for key in everyone:
        if everyone[key] == count:
            code += key
    return code



if __name__ == "__main__":
    unique_groups = process_1("d6/day6_example2.txt")
    sum_total = challenge_1(unique_groups)

    common_total = challenge_1(process_2("d6/day6_input.txt"))
    print(common_total)
    



    
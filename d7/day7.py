import re

def process_1(file_name):
    """
    Purpose:
        Take a .txt file and process so that it returns a list of lists.
    Pre:
        :param file_name: Name of .txt file
    Return:
        An arrayed list where each item is described:
            [0] = bag that contains all other bags
            [1:] = bags that can be held in [0]
    """
    in_file = open(file_name, "r")
    all_bags = []
    for line in in_file:
        first = line.strip().split(" ")
        list_bags = []
        current_bag = ""
        # Check each word, skip if 'continue', add to a string if it doesn't contain bag
        # Otherwise add the current string to the list_bags, and reset the string
        for word in first:
            if "bag" in word:
                list_bags.append(current_bag[:-1]) # removes the extra space
                current_bag = ""
            elif "contain" in word:
                continue
            else:
                current_bag += word + " "
        all_bags.append(list_bags)
    return all_bags

def dict_tree(list_bags):
    dict_tree = {}
    for bag in list_bags:
        dict_tree[bag[0]] = []
        for item in bag[1:]:
            if item != "no other":
                dict_tree[bag[0]].append([item[0], item[2:]])
            else:
                dict_tree[bag[0]].append([0, "none"])
    return dict_tree



if __name__ == "__main__":
    bag_list = process_1("d7/day7_example.txt")
    org_list = dict_tree(bag_list)
    print(org_list)

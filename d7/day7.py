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
    """
    Purpose:
        Take a list of bags, and process into a dictionary
    Pre:
        :param list_bags: An arrayed list where each item is described:
            [0] = bag that contains all other bags
            [1:] = bags that can be held in [0]
    Return:
        Dictionary where key is bag name, and value is a list bags:
            [0] : number of this type of bag that can be stored
            [1] : bag that can be stored
    """
    dict_tree = {}
    for bag in list_bags:
        dict_tree[bag[0]] = []
        for item in bag[1:]:
            if item != "no other":
                dict_tree[bag[0]].append([item[0], item[2:]])
            else:
                dict_tree[bag[0]].append([0, "none"])
    return dict_tree

def find_path(dict_bag):
    """
    Purpose:
        Find how many different types of bags can store a "shiny gold" bag either directly, or indirectly
    Pre:
        :param dict_bag: Return value from dict_tree()
    Return:
        The number of bags that can store "shiny gold" 
    """
    bags = set() # Stores all bags that can store a "shiny gold"
    list_gold = list_of_gold(dict_bag, "shiny gold") # All bags that can directly store a "shiny gold"
    # Use a python list as a queue
    # Remove the first bag from the list, add it "bags", and find any bags that can store this first bag
    # Then extend the list with those bags, and use them as future search terms
    while len(list_gold) > 0:
        bag = list_gold[0]
        bags.add(bag)
        list_gold.remove(bag)
        list_gold.extend( list_of_gold(dict_bag, bag) ) 
    return len(bags)


    
def list_of_gold(dict_bag, search_bag):
    """
    Purpose:
        Find which bags can store a specific bag
    Pre:
        :param dict_bag: Output from dict_tree
        :param search_bag: String rep bag name to search for
    Return:
        List of all bags that can store search_bag
    """
    list_gold = []
    for bag in dict_bag:
        for stored in dict_bag[bag]:
            if search_bag in stored:
                list_gold.append(bag)
    return list_gold



if __name__ == "__main__":
    bag_list = process_1("d7/day7_input.txt")
    org_list = dict_tree(bag_list)
    gold_bags = find_path(org_list)
    print(gold_bags)


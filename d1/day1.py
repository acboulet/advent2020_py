def process(fileName):
    """
    Purpose:
        Processes the given txt file and returns an array consisting of the integer on each line.
    Pre:
        :param fileName: Name of .txt file
    Return:
        A list containing every integer in the .txt file
    """
    inFile = open(fileName, "r")
    values = []
    # converts every line into an integer and adds to inFile
    for line in inFile: 
        values.append(int(line))
    return values

def search(values):
    """
    Purpose:
        Searches a given array for 3 values whos sum is 2020.
    Pre:
        :param values: List of integers
    Return:
        The product of two values within 'values' in which their sum is 2020
    """
    list1 = values
    list2 = values.copy()
    list3 = values.copy()
    # For every value in list1, try adding to every value in list 2
    for n in list1:
        for i in list2:
            for k in list3:
                sumEntry = n+i+k
                # When the value reaches 2020, then append the two values and return the 
                if sumEntry == 2020:
                    return n * i * k

if __name__ == "__main__":
    result = search(process("d1/day1.txt"))
    print(result)
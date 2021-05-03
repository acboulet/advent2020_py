def process(fileName):
    """
    Purpose:
        Process a txt file containing password details, and return a list of all processed passwords
    Pre:
        :param fileName: name of .txt file
    Return:
        A list of password details
            [0] : min value letter can appear
            [1] : most times letteer can appear
            [2] : letter
            [3] : potential password  
    """

    inFile = open(fileName, "r")
    passwordList = []
    # Process the values from each password value
    for line in inFile:
        password = []
        line = line.split() # split where [0] = '#-#'
                            #               [1] = 'a:'
                            #               [2] = 'abcde'
        values = line[0].split("-")
        password.append(int(values[0])) # minimum value
        password.append(int(values[1])) # maximum value
        
        letter = line[1][0]
        password.append(letter)
        code = line[2]
        password.append(code)

        passwordList.append(password)
    return passwordList

def checkPasswords1(listPassword):
    """
    Purpose:
        Checks a list of passwords to see if the match Day 2 criteria.
        The letter must appear >= than the minimum value and <= then maximum value in the password
    Pre:
        :param listPassword: list of passwords to check
                               Each password
                                    [0] : min value letter can appear
                                    [1] : most times letteer can appear
                                    [2] : letter
                                    [3] : potential password 
    Return:
        Number of passwords in the list that meet the criteria
    """
    total = 0
    for password in listPassword:
        letterCount = password[3].count(password[2])
        if (password[0] <= letterCount) and (letterCount <= password[1]):
            total += 1
    return total

def checkPasswords2(listPassword):
    """
     Purpose:
        Checks a list of passwords to see if the match Day 2 - Part 2criteria.
        The letter must appear in position1 or position 2, but not both
    Pre:
        :param listPassword: list of passwords to check
                            Each password
                                    [0] : first position
                                    [1] : second position
                                    [2] : letter
                                    [3] : potential password 
    Return:
        Number of passwords in the list that meet the criteria

    """
    total = 0
    for password in listPassword:
        firstPos = False
        secondPos = False
        # convert positions to indices
        pos1 = password[0] - 1
        pos2 = password[1] - 1

        # if valid index, and letter at position is same as given letter then change to True
        if pos1 < len(password[3]):
            if password[3][pos1] == password[2]:
                firstPos = True
        if pos2 < len(password[3]):
            if password[3][pos2] == password[2]:
                secondPos = True
        
        # If at least one position is true
        if (firstPos or secondPos):
            # If both positions are True though, do nothing
            if (firstPos and secondPos):
                total += 0
            # If only one position was true, then add 1
            else:
                total +=1
    return total
    

if __name__ == "__main__":
    print(checkPasswords1(process("d2/day2.txt")))
    print(checkPasswords2(process("d2/day2.txt")))
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

def checkPasswords(listPassword):
    """
    Purpose:
        Checks a list of passwords to see if the match Day 2 criteria.
        The letter must appear >= than the minimum value and <= then maximum value in the password
    Pre:
        :param listPassword: list of passwords to check
    Return:
        Number of passwords in the list that meet the criteria
    """
    total = 0
    for password in listPassword:
        letterCount = password[3].count(password[2])
        if (password[0] <= letterCount) and (letterCount <= password[1]):
            total += 1
    return total
    




if __name__ == "__main__":
    print(checkPasswords(process("d2/day2.txt")))

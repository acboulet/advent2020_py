# Problem 6 - Solutions taken from /u/Jerslev from Reddit

with open('d6/day6_input.txt', 'r') as fd:
    groups = fd.read().split("\n\n")

    # Part 1
    NumOfYes = 0
    for group in groups:
        answers = group.replace("\n", "")
        NumOfYes += len(set(answers))
    print("Part 1: Number of different questions that got a 'yes'-answer: " + str(NumOfYes))

    # Part 2
    NumOfYes = []
    for group in groups:
        persons = group.split("\n")
        answers = set(persons[0])
        for i in range(1, len(persons)):
            answers &= set(persons[i])  # Updates 'answers' with the entries found in both answers and persons iteration
        NumOfYes.append(len(answers))
    print("Part 2: The amount of persons that all answered 'yes' to the same question is: " + str(sum(NumOfYes)))
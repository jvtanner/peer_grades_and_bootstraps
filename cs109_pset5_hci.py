# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np

# Your Stanford email (fill in the blank): seshwan2@stanford.edu

"""
Starter Code for CS 109 Problem Set 5
Assembled by TA Anand Shankar for David Varodayan's
Winter 2020 course offering.

*************************IMPORTANT*************************
For part_a and part_b and part_c, do NOT modify the name of 
the  functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def part_a(filename):

    total = 0
    with open(filename) as f:
        for line in f:
            total += int(line)
    return float(total/10000)


def part_b(filename, seed=109):

    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###

    score_means = []
    with open(filename) as f:
        all_scores = f.readlines()
    for i in range(len(all_scores)):
        sample_scores = 0
        for y in range(5):
            sample_score = int(np.random.choice(all_scores, 1, replace=True))
            sample_scores += sample_score
        score_means.append(sample_scores/5)
    return float(np.var(score_means))

    ### END YOUR CODE FOR PART (B) ###


def part_c(filename, seed=109):
    """
    filename is the name of a data file, e.g. 
    "peerGrades.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder. Do not alter the 
    seed variable either.

    Just like in part_b, you MUST use np.random.choice.

    Return the variance of the median grade that the 
    control experiment described in the assignment 
    handout would have been given.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (C) ###

    score_medians = []
    with open(filename) as f:
        all_scores = f.readlines()
    for i in range(len(all_scores)):
        sample_scores = []
        for y in range(5):
            sample_score = int(np.random.choice(all_scores, 1, replace=True))
            sample_scores.append(sample_score)
        score_medians.append(sorted(sample_scores)[2])
    return float(np.var(score_medians))

    ### END YOUR CODE FOR PART (C) ###


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("******************************************************")
    print("Calling part_a with filename 'peerGrades.csv'")
    print("\tReturn value was:", part_a('peerGrades.csv'))
    print("******************************************************")

    print("******************************************************")
    print("Calling part_b with filename 'peerGrades.csv'")
    print("\tReturn value was:", part_b('peerGrades.csv'))
    print("******************************************************")

    print("******************************************************")
    print("Calling part_c with filename 'peerGrades.csv'")
    print("\tReturn value was:", part_c('peerGrades.csv'))
    print("******************************************************")

    print("******************************************************")
    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())
    print("******************************************************")

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()

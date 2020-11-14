# Do NOT add any other import statements.
# Don't remove these import statements.
import numpy as np
import sys
import copy

# Your Stanford email (fill in the blank): jvtanner@stanford.edu

"""
Starter Code for CS 109 Problem Set 5
Assembled by TA Anand Shankar for David Varodayan's
Winter 2020 course offering.

*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of 
the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Return the difference in sample means (float) as 
    described in the handout.
    """
    activity1scores = []
    activity2scores = []
    with open(filename, 'r') as f:
        info = f.readlines()
    for line in info:
        data = line.split(",")
        if data[1] == 'activity1':
            activity1scores.append(int(data[2]))
        else:
            activity2scores.append(int(data[2]))

    return abs(np.mean(activity1scores) - np.mean(activity2scores))


def part_b(filename, seed=109):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.

    Return the p-value (float) as described in the handout.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###
    iterations = 10000
    activity1scores = []
    activity2scores = []
    with open(filename, 'r') as f:
        info = f.readlines()
    for line in info:
        data = line.split(",")
        if data[1] == 'activity1':
            # Place two groups of data into separate containers
            activity1scores.append(int(data[2]))
        else:
            activity2scores.append(int(data[2]))
    # Take the difference of the mean from each container
    mean_dif = abs(np.mean(activity1scores) - np.mean(activity2scores))
    both_activities = activity2scores + activity1scores

# So far we have two separate groups of data and we have the mean from each. Obviously, the
    # two means aren't identical. What does this difference in the means tell us about
    # the nature of the two groups? Are the means different because the two groups are
    # really different? or are they similar but they are different by chance?
# How we solve this: Let's throw the two groups into one bucket. Maybe one group was
    # bigger or small than the other, doesn't matter for now. Once they are in one bucket,
    # we take two sample sets IDENTICAL IN LENGTH TO THE ORIGINAL BUCKET SIZES, RESPECTIVELY.
    # Then we take the mean of these two groups, and find the difference, just like last time.
    # Compare the difference this time, when the buckets are combined, to the difference last
    # time, when the buckets were separate. Is the difference lesser now?
# What are we doing here?
    # Obviously, if we're pulling from the same bucket, we would expect the difference in mean
    # to be pretty small. We would expect the difference to be EQUALLY SMALL with the two separate
    # buckets if they were IDENTICAL (or close to it).
# If after comparing the two mean differences between the separate-bucket-scenario and the
    # combined-bucket-scenario 10,000 times and only 500 times was the combined-bucket higher than the
    # separate-bucket (5% of the time), then we can say that the two original buckets are
    # likely distinct with a p-value of .05

    count = 0
    for i in range(iterations):
        act1_sample = np.random.choice(both_activities, len(activity1scores), replace=True)
        act2_sample = np.random.choice(both_activities, len(activity2scores), replace=True)
        if abs(np.mean(act2_sample) - np.mean(act1_sample)) >= mean_dif:
            count += 1
    return float(count/iterations)
    ### END YOUR CODE FOR PART (B) ###


def optional_function(filename1, filename2):
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    np.random.seed(109)

    my_dict = {}
    with open(filename2, 'r') as g:
        contentB = g.readlines()
    for line2 in contentB:
        answer2 = line2.split(",")
        # for each line, storing the amount of background for each person
        x = answer2[1]
        # create a dict where the ID is the key and the experience is the value
        my_dict[answer2[0]] = x[0:len(x)-1]

    with open(filename1, 'r') as f:
        content = f.readlines()
    activity1L = []
    activity1M = []
    activity1A = []
    activity2L = []
    activity2M = []
    activity2A = []
    for line in content:
        answer = line.split(",")

    # instead of two buckets, now we have 6 buckets
        if answer[1] == "activity1" and my_dict[answer[0]] == "less":
            activity1L.append(int(answer[2]))
        elif answer[1] == "activity1" and my_dict[answer[0]] == "more":
            activity1M.append(int(answer[2]))
        elif answer[1] == "activity1" and my_dict[answer[0]] == "average":
            activity1A.append(int(answer[2]))
        elif answer[1] == "activity2" and my_dict[answer[0]] == "less":
            activity2L.append(int(answer[2]))
        elif answer[1] == "activity2" and my_dict[answer[0]] == "more":
            activity2M.append(int(answer[2]))
        elif answer[1] == "activity2" and my_dict[answer[0]] == "average":
            activity2A.append(int(answer[2]))

# Finding the difference between the means of the groups
    differenceLess = abs(np.mean(activity2L) - np.mean(activity1L))
    differenceMore = abs(np.mean(activity2M) - np.mean(activity1M))
    differenceAverage = abs(np.mean(activity2A) - np.mean(activity1A))

    print('Difference - less: ', differenceLess)
    print('Difference - more: ', differenceMore)
    print('Difference - average: ', differenceAverage)

# Pool the groups you want to compare into joint buckets
    uni_sample_avg = activity1A + activity2A
    uni_sample_more = activity1M + activity2M
    uni_sample_less = activity1L + activity2L

    count_more = 0
    count_avg = 0
    count_less = 0

    for i in range(0, 10000):
        a1_less_resample = np.random.choice(uni_sample_less, len(activity1L), replace=True)
        a2_less_resample = np.random.choice(uni_sample_less, len(activity2L), replace=True)
        dif_less = np.abs(np.mean(a1_less_resample) - np.mean(a2_less_resample))
        if dif_less >= differenceLess:
            count_less += 1

    for j in range(0, 10000):
        a1_more_resample = np.random.choice(uni_sample_more, len(activity1M), replace=True)
        a2_more_resample = np.random.choice(uni_sample_more, len(activity2M), replace=True)
        dif_more = np.abs(np.mean(a1_more_resample) - np.mean(a2_more_resample))
        if dif_more >= differenceMore:
            count_more += 1

    for k in range(0, 10000):
        a1_avg_resample = np.random.choice(uni_sample_avg, len(activity1A), replace=True)
        a2_avg_resample = np.random.choice(uni_sample_avg, len(activity2A), replace=True)
        dif_avg = np.abs(np.mean(a1_avg_resample) - np.mean(a2_avg_resample))
        if dif_avg >= differenceAverage:
            count_avg += 1

    print("p value for num greaterLess: ", float(count_less / 10000))
    print("p value for num greaterMore: ", float(count_more / 10000))
    print("p value for num greaterAvg: ", float(count_avg / 10000))


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    args = sys.argv[1:]
    filename1 = args[0]
    filename2 = args[1]
    optional_function(filename1, filename2)


    print("****************************************************")
    print("Calling part_a with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_a('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling part_b with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_b('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())
    print("****************************************************")


    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()

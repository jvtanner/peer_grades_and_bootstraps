# peer grades and bootstrapping


7. [Coding + Written] Stanford’s HCI class runs a massive online class that was taken by ten
thousand students. The class used peer assessment to evaluate students’ work. We are going to use their data to learn more about peer graders. In the class, each student has their work evaluated by 5 peers and every student is asked to evaluate 6 assignments: five peers and the “control assignment” (the graders were unaware of which assignment was the control). All 10,000 students evaluated the same control assignment, and the scores they gave are in the file peerGrades.csv. You may use simulations to solve any part of this question.
Here are some rules that apply to all the coding questions:

• Write your answers in the relevant functions of the file cs109_pset5_hci.py, which
you can download from the course website. Do not rename this file. For this question, submit only this file.
• Your code will be autograded.
• Do not use global variables.
• You may define helper functions if you wish.

a. [Coding] What is the sample mean of the 10,000 grades to the control assignment?
Implement the part_a function, which should return this quantity as a float.

For parts (b) and (c), you’ll need to run some simulations. To get credit from the autograder, you’re required to abide by the following guidelines:
• Run the algorithm for exactly 10,000 iterations.
• You’ll need to draw random samples with replacement from an array of grades. To do so,
you must use the np.random.choice function, which you can call like so: sample = np.random.choice(name-of-array, size-of-random-sample, replace=True). Do not use any other function to generate random samples.
• Use the np.mean, np.median, and np.var functions to calculate the mean, median, and
variance of a list or numpy array.

b. [Coding] Students could be given a final score which is the mean of the 5 grades given
by their peers. Imagine the control experiment had only received 5 peer-grades. What
is the variance of the mean grade that the control experiment would have been given?
Implement the part_b function, which should return this quantity as a float.

c. [Coding] Students could be given a final score which is the median of the 5 grades given
by their peers. Suppose the control experiment had only received 5 peer-grades. What
is the variance of the median grade that the control experiment would have been given?
Implement the part_c function, which should return this quantity as a float.

d. [Written] Would you use the mean or the median of 5 peer grades to assign scores in
the online version of Stanford’s HCI class? Hint: it might help to visualize the scores.
Feel free to write code to help you answer this question, but for this question we’ll solely
evaluate your written answer in the PDF that you upload to Gradescope.






8. [Coding + Written] In this problem you are going to learn how to use and misuse p-values
for experiments that are called A/B tests. These experiments are ubiquitous. They are a staple
of both scientific experiments and user interaction design.
Suppose you are working at Coursera on new ways of teaching a concept in probability. You
have two different learning activities activity1 and activity2 and you want to figure out
which activity leads to better learning outcomes.
Over a two-week period, you randomly assign each student to be given either activity1
or activity2. You then evaluate each student’s learning outcomes by asking them to solve
a set of problems. The data (the activity shown to each student and their measured learning
outcomes) are found in the file learningOutcomes.csv.

a. [Coding] What is the difference in sample means of learning outcomes between students
who were given activity1 and students who were given activity2? Write your answer
in the part_a function, which should return a float (i.e. the difference in sample means). 

b. [Coding] Write code to estimate the p-value (using the bootstrap method) for the observed
difference in means reported in part (a). In other words: assuming that the learning
outcomes for students who had been given activity1 and activity2 were identically
distributed, what is the probability that you could have sampled two groups of students
such that you could have observed a difference of means as extreme, or more extreme,
than the one calculated from your data in part (a)? Write your answer in the part_b
function, which should return a float. Here are some guidelines to follow:

• Just like in the previous problem, you are required to use the np.random.choice
method with replace=True to generate random samples.
• For the bootstrap algorithm, you should use 10,000 iterations, i.e. you should resam-
ple 10,000 times.
• If you have two lists a and b, you can create a new list containing all the elements of
a followed by all the elements of b by writing a + b
outcome between activity1 and activity2, and the p-value of that difference.



Scientific journals have traditionally accepted an experiment’s result as “statistically signif- icant” if the p-value is below 0.05. By definition, this standard means that 5% of findings published in these journals are in fact not true, but just false positives. The scientific com- munity is beginning to move away from using arbitrary p-value thresholds to determine whether a result is publishable. For example, see this 2019 editorial in the journal Nature: https://www.nature.com/articles/d41586-019-00874-8.
You are now troubled by the p-value you obtained in part (b), so you decide to delve deeper. You investigate whether learning outcomes differed based on the background experience of students. The file background.csv stores the background of each student as one of three labels: more experience, average experience, less experience.

c. [Written] For each of the three backgrounds, calculate a difference in means in learning outcome between activity1 and activity2, and the p-value of that difference. You’ll almost certainly need to write code in this question, and we’ve provided an optional_function that you can use, which gets called by our provided main method. However, we won’t grade any code for this part. We’ll only grade what you include in your answer PDF.
d. [Written] Your manager at Coursera is concerned that you have been “p-hacking,” which
is also known as data dredging: https://en.wikipedia.org/wiki/Data_dredging. In one sentence, explain why your results in part (c) are not the result of p-hacking.






# -*- coding: utf-8 -*-
"""Project 48

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dhKYYmtOcXqKT7p6mr6BB6ygBSxP5uBv

### Instructions

#### Activity 1: Calculate the probability of a random variable

Calculate the probability of solving 35 questions correctly by fluke in an MCQ test having 250 questions (each question have 4 options).

**Steps to follow:**

1. Create a function to calculate the factorial of a number. It takes an integer as an input for which the factorial value needs to be calculated.

2. Create a function to calculate the probability of a random variable. It takes the total number of trials `num_trials`, a random variable `random_var` and the probability of success `prob_success` as inputs.

   - First, calculate the value of ${}^nC_{r} = \frac{n!}{(n - r)! \times r!}$ and store in the `num_trials_choose_random_var` variable.

   - Then calculate the probability of random variable $P(X = r) = {}^nC_r \times s^r \times f^{n - r}$ and store in the `prob_random_var` variable.

   - The function returns the value of `prob_random_var`. 

   - Note that the probability of failure is `1 - prob_success`.
"""

# Write your solution here
# Function to calculate the factorial value of a number 'n'.
def factorial(num):
  factorial = 1
  if num < 0:
    return "Undefined."
  else:
    while num > 0:
      factorial *= num
      num -= 1
    return factorial

# Function to calculate the probability of a random variable X = r.
def prob_random_var(num_trials, random_var, prob_success):
  num_trials_choose_random_var = factorial(num_trials) / ((factorial(num_trials - random_var)) * (factorial(random_var))) # nCr 
  prob_random_var = num_trials_choose_random_var * (prob_success ** random_var) * ((1 - prob_success) ** (num_trials - random_var))
  return prob_random_var

# The probability of solving say 35 questions correctly by fluke in an MCQ test having 250 questions
prob_random_var(250, 35, 0.25)

"""**Question**: What is the probability of solving say 35 questions correctly by fluke in an MCQ test having 250 questions?

**Answers**: 7.85

---

#### Activity 2: Expected value

Find out the average number of questions that can be solved correctly by fluke in an MCQ test having 300 questions.
"""

# Find the average number of questions that can be solved correctly by fluke in an MCQ test having 300 questions.
import numpy as np
rand_var = np.arange(301)
prob_rand_var_list = [prob_random_var(300, i, 0.25) for i in range(301)]
expected_val = np.sum(rand_var * np.array(prob_rand_var_list))
expected_val

"""**Question**: How many average number questions can be solved correctly by fluke in an MCQ test having 300 questions?

**Answers**: On an average, you are expected to solve 75 questions correctly by fluke in an MCQ test having 300 questions.

**Hints**:

1. Use the concept of expected value. The expected value is the sum of the product of the random variables with their corresponding probabilities.

2. Let $X$ be a random variable denoting $N$ events $x_1, x_2, x_3 \dots x_N$ and let $p(x_1), p(x_2), p(x_3) \dots p(x_N)$ be their corresponding probabilities, then the expected value $E(X)$ is given by 

$$E(X) = x_1 p(x_1) + x_2 p(x_2) + x_3 p(x_3) + \dots + x_N p(x_N)$$

---
"""
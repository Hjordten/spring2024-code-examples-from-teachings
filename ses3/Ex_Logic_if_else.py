# Ex: Logic if / else
# You are creating a simple grade evaluation system for a class. The system should take an integer input, which represents a student’s score, and then return a grade according to the following criteria:
#
# If the score is 90 or higher, the grade should be “A”.
#
# If the score is between 80 and 89 (inclusive), the grade should be “B”.
#
# If the score is between 70 and 79 (inclusive), the grade should be “C”.
#
# If the score is between 60 and 69 (inclusive), the grade should be “D”.
#
# If the score is below 60, the grade should be “F”.
#
# Additionally, if the score is outside the range of 0 to 100, the system should return “Invalid score”.
#
# Your task is to write a Python function that takes a score as an input and returns the corresponding grade. You are welcome to write this in a straight forward if/else approch, but you should also write it in a one-liner using a ternary operator.
#
# Solution: When you are done, copy/paste this exercise description + your solution into ChatGpt, asking it for feed back on how you solved the problem and where you could improve your solution.

def evaluate_grade(score):
    if score <  0 or score >  100:
        return "Invalid score"
    elif score >=  90:
        return "A"
    elif score >=  80:
        return "B"
    elif score >=  70:
        return "C"
    elif score >=  60:
        return "D"
    else:
        return "F"

# Example usage:
student_score =  85
grade = evaluate_grade(student_score)
print(grade)  # Output: B


def evaluate_grade(score):
    return "Invalid score" if score <  0 or score >  100 else ("A" if score >=  90 else ("B" if score >=  80 else ("C" if score >=  70 else ("D" if score >=  60 else "F"))))

# Example usage remains the same:
student_score =  85
grade = evaluate_grade(student_score)
print(grade)  # Output: B

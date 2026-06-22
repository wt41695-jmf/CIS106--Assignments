# This returns total points and average score.

def compute_scores(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score


last_name = input("Enter student's last name: ")
score1 = float(input("Enter exam score 1: "))
score2 = float(input("Enter exam score 2: "))
score3 = float(input("Enter exam score 3: "))

total_points, average_score = compute_scores(score1, score2, score3)

print("Student Last Name:", last_name)
print("Total Points:", format(total_points, ".2f"))
print("Average Exam Score:", format(average_score, ".2f"))

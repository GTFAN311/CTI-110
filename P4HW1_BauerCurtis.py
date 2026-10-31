#Curtis Bauer
#30 Oct 2026
#P4HW1
#Score information calculator

#Ask user to input number of scores
#Create a loop to collect the number of scores from user
#Ensure the score is between 0 and 100. If not, notify the user and ask for a valid score
#Will need more than one loop

score_num = int(input("How many scores do you want to enter? "))
print()    

scores_list = []   

for i in range(1, score_num + 1):
    score_input = input(f"Enter score #{i}: ")
    score = float(score_input)
    
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score_input = input(f"Enter score #{i} again: ")
        score = float(score_input)
    
    scores_list.append(score)
       
print()
print()

low_score = min(scores_list)

mod_list = scores_list.copy()
mod_list.remove(low_score)

if len(mod_list) > 0:
    avg = sum(mod_list) / len(mod_list)
else:
    avg = 0.0
    
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{'-'*16}Results{'-'*17}")
print(f"Lowest Score   : {low_score:.1f}")
print(f"Modified List  : {mod_list}")
print(f"Scores Average : {avg:.2f}")
print(f"Grade          : {grade}")
print(f"{'_'*40}")
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

true_score = 0
love_score = 0
both_names = name1.lower() + name2.lower()
true_score += both_names.count("t")
true_score += both_names.count("r")
true_score += both_names.count("u")
true_score += both_names.count("e")
love_score += both_names.count("l")
love_score += both_names.count("o")
love_score += both_names.count("v")
love_score += both_names.count("e")
full_score = (str(true_score) + str(love_score))
full_score_int = int(full_score)
if full_score_int >= 40 and full_score_int <= 50:
  print(f"Your score is {full_score}, you are alright together.")
elif full_score_int < 10 or full_score_int > 90:
  print(f"Your score is {full_score}, you go together like coke and mentos.")
else:
  print(f"Your score is {full_score}.")
questions = ("How many bones are there in human body? ",
             "What animal lays the biggest egg? ",
             "What is the most abundant gas in the earth's atmosphere? ")

options = (("A. 206", "B.207", "C.208", "D.209"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D.Ostrich"),
           ("A. Nitrogen", "B.Oxygen", "C. CO2", "D. Hydrogen"))

answers = ("A", "D", "A")

guesses = []
question_num = 0
score = 0


for i in questions:
    print("_____________________________")
    print(i)
    for x in options[question_num]:
        print(x)
    guess = input("Enter (A, B, C, D): ").upper()
    while not guess in ['A','B','C','D']:
        guess = input("Please enter A, B, C, D: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
    question_num +=1
print(f"Your score is {score}/5.")

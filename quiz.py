from database import save_score
name = input("Enter your name: ")
print("Welcome", name)
score = 0
questions = [
    {
        "question": " What is the correct file extension for Python files?",
        "options": ["A. .java", "B. .html", "C. .py", "D. .cpp"],
        "answer": "C"
    },
    {
        "question": " Who developed Python?",
        "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": " Which function is used to display output in Python?",
        "options": ["A. display()", "B. print()", "C. show()", "D. echo()"],
        "answer": "B"
    },
    {
        "question": " Which function is used to get input from the user?",
        "options": ["A. input()", "B. scan()", "C. read()", "D. get()"],
        "answer": "A"
    },
    {
        "question": " Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. <!-- -->"],
        "answer": "B"
    },
    {
        "question": " Which data type stores whole numbers?",
        "options": ["A. float", "B. str", "C. int", "D. bool"],
        "answer": "C"
    },
    {
        "question": " Which operator is used for multiplication?",
        "options": ["A. +", "B. -", "C. *", "D. /"],
        "answer": "C"
    },
    {
        "question": " Which keyword is used to create a function?",
        "options": ["A. function", "B. fun", "C. define", "D. def"],
        "answer": "D"
    },
    {
        "question": " Which loop repeats a block of code while a condition is true?",
        "options": ["A. for", "B. while", "C. if", "D. switch"],
        "answer": "B"
    },
    {
        "question": " Which keyword is used for conditional statements?",
        "options": ["A. loop", "B. case", "C. if", "D. repeat"],
        "answer": "C"
    },
    {
        "question": " Which data type is used to store True or False values?",
        "options": ["A. str", "B. bool", "C. int", "D. float"],
        "answer": "B"
    },
    {
        "question": " Which brackets are used for a Python list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C"
    },
    {
        "question": " Which brackets are used for a Python dictionary?",
        "options": ["A. {}", "B. []", "C. ()", "D. <>"],
        "answer": "A"
    },
    {
        "question": " Which keyword is used to exit a loop?",
        "options": ["A. continue", "B. break", "C. stop", "D. exit"],
        "answer": "B"
    },
    {
        "question": " Which function returns the length of a list or string?",
        "options": ["A. size()", "B. count()", "C. len()", "D. length()"],
        "answer": "C"
    },
    {
        "question": " Which keyword is used to define a class in Python?",
        "options": ["A. object", "B. class", "C. define", "D. new"],
        "answer": "B"
    },
    {
        "question": " Which of these is a mutable data type?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. error", "B. except", "C. catch", "D. throw"],
        "answer": "B"
    },
    {
        "question": " Which keyword is used to import a module?",
        "options": ["A. include", "B. using", "C. import", "D. module"],
        "answer": "C"
    },
    {
        "question": " Which operator is used for exponentiation (power)?",
        "options": ["A. ^", "B. **", "C. %", "D. //"],
        "answer": "B"
    }
]
print("===== PYTHON QUIZ =====")

score = 0
import random
random.shuffle(questions)
for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print(" Correct!")
        score += 1
    else:
        print(" Wrong!")
        print("Correct Answer:", q["answer"])

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))
percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")
file = open("score.txt","a" )
file.write(name + " - " + str(score) + "/" + str(len(questions)) + "\n")
file.close()
print("File location checked!")
if percentage >= 90:
    grade = "A"
    print("grade:A")
    print("Excellent! ")
elif percentage >= 75:
    grade = "B"
    print("grade:B")
    print("Very Good! ")
elif percentage >= 50:
    grade = "C"
    print("grade:C")
    print("Good! ")
else:
    grade = "D"
    print("grade:D")
    print("Need More Practice! ")
save_score(name,score,len(questions),grade ,percentage)
print("Thank you for playing,", name)
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

score = 0

print("Welcome to Quiz Game!\n")

for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Your Score:", score)

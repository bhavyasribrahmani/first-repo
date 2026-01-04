
from functools import reduce
name=input("name: ")
print("Hello",name, "Ready to play Quick python Quiz")
print("There are 9 Questions total, after attempting all questions we get score")
print("Python Quiz")
# Quiz questions stored in nested lists
quiz = [
    ["What is the capital of India?", ["a) Delhi", "b) Mumbai", "c) Kolkata", "d) Chennai"], "a"],
    ["Which language is used for web development?", ["a) Python", "b) HTML", "c) C++", "d) Java"], "b"],
    ["2 + 2 = ?", ["a) 3", "b) 4", "c) 5", "d) 6"], "b"],
    ["Which planet is known as Red Planet?", ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"], "b"],
    ["2^7 = ?",["a) 564", "b) 1024", "c) 128", "d) 64"],"c"],
    ["What is the largest ocean in the world?", ["a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"], "c"],
    ["Which device is used to measure temperature?", ["a) Barometer", "b) Thermometer", "c) Hygrometer", "d) Altimeter"], "b"],
    ["Which gas do humans need to breathe?", ["a) Carbon Dioxide", "b) Oxygen", "c) Nitrogen", "d) Hydrogen"], "b"],
    ["Which is the fastest land animal?", ["a) Lion", "b) Tiger", "c) Cheetah", "d) Horse"], "c"]
]

# Track highest scores
highest_scores = []

# Function to ask questions
def ask_questions():
    answers = []
    print("\n--- Quiz Start ---\n")
    for i, q in enumerate(quiz):
        print(f"Q{i+1}: {q[0]}")
        for option in q[1]:
            print(option)
        ans = input("Your answer (a/b/c/d): ").strip().lower()   # string methods
        answers.append(ans)
    return answers

# Function to calculate score using map
def calculate_score(user_answers):
    results = list(map(lambda ua, q: ua == q[2], user_answers, quiz))
    scores = list(map(lambda r: 1 if r else 0, results))
    return results, scores

# Function to compute total score using reduce
def total_score(scores):
    return reduce(lambda a, b: a + b, scores)

# Recursive function to replay quiz
def play_quiz():
    user_answers = ask_questions()
    results, scores = calculate_score(user_answers)
    score = total_score(scores)
    percentage = (score / len(quiz)) * 100

    # Question-by-question result
    print("\n--- Results ---")
    for i, res in enumerate(results):
        if res:
            print(f"Q{i+1}: Correct ✅")
        else:
            print(f"Q{i+1}: Wrong ❌")

    # Final output
    print(f"\nTotal Score: {score}/{len(quiz)}")
    print(f"Percentage: {percentage:.2f}%")
    if percentage >= 50:#unicode  U+1F389 🎉
        print("Result: Pass 🎉")
    else:#unicode U+1F622 --😢
        print("Result: Fail 😢")

    # Track highest score
    highest_scores.append(score)
    print(f"Highest Score so far: {max(highest_scores)}")

    # Replay option using recursion
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play_quiz()
    else:
        print("\nThanks for playing! Goodbye 👋")

# Start the game
play_quiz()
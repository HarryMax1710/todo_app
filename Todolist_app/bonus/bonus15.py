import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for q in data:
    print(q["question"])
    for index, alternative in enumerate(q["alternatives"]):
        print(index+1,"-",alternative)

    user_input = int(input("Enter your answer: "))
    q["user_input"] = user_input

score = 0
for index, q in enumerate(data):
    if q["user_input"] == q["correct_answer"]:
        score = score + 1
        ans = "Correct Answer"
    else:
        ans = "Wrong Answer"

    result = f"{index + 1} {ans} - Your answer: {q['user_input']}, " \
            f"Correct answer: {q['correct_answer']}"
    print(result)

print(score, "/", len(data))
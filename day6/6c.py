def count_similar_answers(answers, people):
    similar_answers = set(
        filter(lambda answer: answers.count(answer) == people, answers)
    )
    return len(similar_answers)


count = 0

with open("6.txt") as input:
    answers = []
    people = 0
    for line in input.readlines():
        if line == "\n":
            count += count_similar_answers(answers, people)
            people = 0
            answers = []
        else:
            people += 1
            answers = answers + list(line.strip("\n"))
    count += count_similar_answers(answers, people)

print(count)
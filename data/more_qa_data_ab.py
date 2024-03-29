from datasets import load_dataset
from itertools import product
import json
from random import shuffle

A_B = []

truthful_qa_rows = load_dataset("truthful_qa", "generation", split="validation")

for item in truthful_qa_rows:
    question = item["question"].strip()
    correct_answers = item["correct_answers"]
    incorrect_answers = item["incorrect_answers"]
    for answers in product(correct_answers, incorrect_answers):
        answers = list(answers)
        correct_answer = answers[0]
        shuffle(answers)
        if answers[0] == correct_answer:
            answer_matching_behavior = "(A)"
            answer_not_matching_behavior = "(B)"
        else:
            answer_matching_behavior = "(B)"
            answer_not_matching_behavior = "(A)"
        full_question = (
            f"{question}\n\nChoices:\n(A) {answers[0]}\n(B) {answers[1]}"
        )
        A_B.append(
            {
                "question": full_question,
                "answer_matching_behavior": answer_matching_behavior,
                "answer_not_matching_behavior": answer_not_matching_behavior,
            }
        )

print("Number of samples:", len(A_B))
shuffle(A_B)
with open(f"more_qa_data_A_B.json", "w") as f:
    json.dump(A_B, f)

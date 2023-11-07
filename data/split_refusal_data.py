import json
from random import shuffle


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def create_n_random_splits(data_path, n=2):
    with open(data_path, "r") as f:
        data = json.load(f)
        shuffle(data)
        for split_idx, split_data in enumerate(split(data, n)):
            with open(f"refusal_data_{n}splits_{split_idx}.json", "w") as s:
                json.dump(split_data, s, indent=4)


full_data_path = "refusal_data.json"
num_splits = 2

create_n_random_splits(full_data_path, num_splits)

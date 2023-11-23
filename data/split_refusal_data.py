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


def create_cat_splits(data_path):
    with open(data_path, "r") as f:
        data = json.load(f)
        for cat_idx in [1, 2, 3]:
            cat_items = []
            for item in data:
                if item["category"] == cat_idx:
                    cat_items.append(item)
            print(f"Number of items in category {cat_idx}: {len(cat_items)}")
            with open(f"refusal_data_cat{cat_idx}.json", "w") as s:
                json.dump(cat_items, s, indent=4)


full_data_path = "refusal_data.json"
create_cat_splits(full_data_path)

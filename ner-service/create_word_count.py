import csv
import json
import os

CATEGORIES_DIR = "src/entities"
os.makedirs(CATEGORIES_DIR, exist_ok=True)


def main():
    word_counts = {}
    with open("off_categories.tsv", "r") as f:
        for line in csv.reader(f, delimiter="\t"):
            key = line[1]

            key_split = key.split(":")
            if len(key_split) > 1:
                entity = key_split[1]
            else:
                entity = key_split[0]

            for word in entity.split():
                word = word.lower()
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    with open(os.path.join(CATEGORIES_DIR, "word_counts.json"), "w") as f:
        json.dump(word_counts, f)


if __name__ == '__main__':
    main()

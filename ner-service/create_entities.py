import os
import csv
import json

from pattern.en import pluralize, singularize

CATEGORIES_DIR = "src/service/entities"
os.makedirs(CATEGORIES_DIR, exist_ok=True)


def main():
    data = {}
    count = 0
    with open("off_categories.tsv", "r") as f:
        for line in csv.reader(f, delimiter="\t"):
            if count > 1:
                key = line[1]
                lang = "en"
                key_split = key.split(":")
                value = key_split[0]
                if len(key_split) > 1:
                    lang = key_split[0]
                    value = key_split[1]

                entity = value.lower().replace("-", " ")

                if lang not in data:
                    data[lang] = {}

                if lang == "en":
                    data[lang].update(
                        {
                            pluralize(entity): key,
                            singularize(entity): key,
                            entity: key
                        }
                    )
                else:
                    data[lang].update(
                        {
                            entity: key
                        }
                    )

            count += 1

    for lang, entities in data.items():
        with open(os.path.join(CATEGORIES_DIR, f"{lang}.json"), "w", encoding="utf-8") as f:
            json.dump(entities, f, ensure_ascii=False)


if __name__ == '__main__':
    main()

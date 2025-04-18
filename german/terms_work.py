"""
Module for working with terms and examples from CSV files.
"""

def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms

def get_examples():
    examples = []
    with open("./data/examples.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            examples.append([cnt, term, definition])
            cnt += 1
    return examples

def write_term(new_term, new_definition):
    new_term_line = f"{new_term};{new_definition};user"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))
        

def write_example(new_example, new_definition):
    new_example_line = f"{new_example};{new_definition};user"
    with open("./data/examples.csv", "r", encoding="utf-8") as f:
        existing_examples = [l.strip("\n") for l in f.readlines()]
        title = existing_examples[0]
        old_examples = existing_examples[1:]
    examples_sorted = old_examples + [new_example_line]
    examples_sorted.sort()
    new_examples = [title] + examples_sorted
    with open("./data/examples.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_examples))


def get_stats():
    db_terms = 0
    user_terms = 0
    defin_len = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            term, defin, added_by = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1
    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "words_avg": sum(defin_len)/len(defin_len),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    return stats

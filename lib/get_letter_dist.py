import string


def get_letter_dist(words):
    letter_counts = dict([letter, 0] for letter in string.ascii_lowercase)

    for word in words:
        for letter in word:
            if letter in string.ascii_letters:
                letter_counts[letter.lower()] += 1

    max_count = max(letter_counts.values())
    dist = dict(
        [letter, count / max_count] for letter, count in letter_counts.items()
    )

    return (letter_counts, dist)

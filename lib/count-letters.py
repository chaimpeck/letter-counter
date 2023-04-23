import sys
import string
import math
import random


NUM_PLAYERS = 4
MAX_PLAYER_TILES = 16
NUM_ROUNDS = 4

def get_letter_dist(words):
    letter_counts = dict([letter, 0] for letter in string.ascii_lowercase)

    for word in words:
        for letter in word:
            if letter in string.ascii_letters:
                letter_counts[letter.lower()] += 1

    total_count = sum(letter_counts.values())
    return dict([letter, count/total_count] for letter, count in letter_counts.items())

def get_tile_set(letter_dist, mult=100):
    tile_set = []
    for letter, dist in letter_dist.items():
        tile_set.extend([letter] * math.ceil(dist * mult))

    return tile_set

def find_words(letters, words):
    found_words = []
    for word in words:
        word_letters  = list(word)
        for letter in letters:
            if letter in word_letters:
                word_letters.remove(letter)

        if len(word_letters) == 0:
            found_words.append(word)

    return found_words


def main(argv):
    with open(argv[1]) as f:
        words = list(filter(len, f.read().splitlines()))

    letter_dist = get_letter_dist(words)

    tile_set = get_tile_set(letter_dist)
    print("New Game! Got a tile set of size {len(tile_set)}}. Now shuffling tiles")
    random.shuffle(tile_set)

    print(f"Starting tileset now has size {len(tile_set)} and consists of {''.join(tile_set)}")

    # Start with all players having empty sets of tiles
    player_tiles = [[] for _ in range(NUM_PLAYERS)]

    for round_number in range(NUM_ROUNDS):
        print(f"Round {round_number} begins!")
        # Each player draws up to MAX_PLAYER_TILES on their turn
        for player in range(NUM_PLAYERS):
            print(f"\tPlayer {player + 1}")

            number_of_tiles_to_draw = MAX_PLAYER_TILES - len(player_tiles[player])
            print(f"\t\tSelects {number_of_tiles_to_draw} tiles")
            player_tiles[player].extend([tile_set.pop() for _ in
                                         range(number_of_tiles_to_draw)])
            print(f"\t\tPlayer {player + 1} now has tiles: {''.join(player_tiles[player])}")
            found_words = find_words(player_tiles[player], words)
            if len(found_words) == 0:
                print(f"\t\tNo matched words")
                # TODO: What happens when there are no matches? Draw new tiles?
            else:
                print(f"\t\tFound words: {', '.join(found_words)}")
                play_word = random.choice(found_words)
                print(f"\t\tPlaying \"{play_word}\" and putting the word back into the pile")
                for letter in play_word:
                    player_tiles[player].pop(player_tiles[player].index(letter))
                    tile_set.append(letter)
                print("\t\tShuffling tile set")
                random.shuffle(tile_set)

        print(f"*** At the end of round {round_number} tileset now has " \
              f"{len(tile_set)} tiles and consists of {''.join(tile_set)} ***")
        print()

    # TODO: report on statistics of number of matched words, etc


import dill

from .util import tokenize
from itertools import permutations


def load(file_path):
    with open(file_path, "rb") as fp:
        try:
            config = dill.load(fp)
        except FileNotFoundError:
            print(f"File not found {file_path}")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")

    return config


def translate(text, config, trg_code):
    # load model
    sorted_t = load(f"{config}sorted_model_{trg_code}.pkl")
    unigrams = load(f"{config}unigrams_{trg_code}.pkl")
    bigrams = load(f"{config}bigrams_{trg_code}.pkl")

    # tokenize
    token_stores = tokenize(text)
    tokens_words = token_stores

    # translate
    translated_words = []
    for token in tokens_words:
        translation = find_translation(token, sorted_t)
        if translation != "":
            translated_words.append(translation)

    perm = permutations(translated_words)
    best_seq = translated_words
    best_prob = -1

    for seq in perm:
        prob = get_prob(seq, bigrams, unigrams)
        if prob > best_prob:
            best_prob = prob
            best_seq = seq

    return best_seq, best_prob


def find_translation(src_token, sorted_t):
    for element in sorted_t:
        if element[0][0].lower() == src_token:
            return element[0][1]
    return src_token


def get_prob(seq, bigrams, unigrams):
    if len(seq) < 2:
        return 1
    score = 0
    token_a = ''
    unigrams_count = len(unigrams)
    for trg_token in seq:
        token_b = trg_token
        if (token_a, token_b) not in bigrams:
            if token_b not in unigrams:
                # Handle OOV words by applying Laplace smoothing
                score += 1.0 / (unigrams_count + len(unigrams))
            else:
                score += unigrams[token_b] / unigrams_count
        else:
            base_token_count = 0
            if token_a in unigrams:
                base_token_count = unigrams[token_a]
            score += (bigrams[(token_a, token_b)] + 1) / (base_token_count + unigrams_count)
        token_a = token_b
    return score

def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]

def is_anagram(word, candidate):
    word_lwr = word.lower()
    candidate_lwr = candidate.lower()
    return sorted(word_lwr) == sorted(candidate_lwr) and word_lwr != candidate_lwr
    
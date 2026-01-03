def get_num_words(t):
    num_words_list = t.split()
    num_words=len(num_words_list)
    print(f"Found {num_words} total words")

def count_chars_in_string(t):
    char_counts = {}
    t = t.lower()
    for char in t:
        if char in char_counts and char.isalnum():
            char_counts[char] += 1
        elif char.isalnum():
            char_counts[char] = 1
    return char_counts

def dict_to_sorted_list(d):
    new_list = []
    if d is not None:
        new_list = list(d.items())
        new_list.sort()
    return new_list
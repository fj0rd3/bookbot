def count_words(book):
    words = book.split()
    return len(words)


def count_chars(book):
    dict = {}
    for char in book:
        if char.lower() in dict:
            dict[char.lower()] += 1
        else:
            dict[char.lower()] = 1
    return dict


def sort_dict(dict):
    arr = []
    for k, v in dict.items():
        arr.append({"char": k, "num": v})
    arr.sort(key=lambda x: x["num"], reverse=True)
    return arr

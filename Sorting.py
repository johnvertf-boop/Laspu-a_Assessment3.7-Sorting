full_name = "Johnvert Laspuña"

# alphabet order (naa ang Ñ human sa N)
ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# ---------- step 1: build the unsorted array ----------
# keep only letters (no symbols), and discard duplicate letters
def build_unsorted(name):
    letters = []
    for ch in name.upper():
        if ch in ALPHABET and ch not in letters:
            letters.append(ch)
    return letters


# ---------- step 2: Insertion Sort ----------
# take one letter at a time and insert it in the correct place
# of the already-sorted part on the left
def insertion_sort(arr):
    result = arr.copy()            # copy, so the unsorted array stays the same
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and ALPHABET.index(result[j]) > ALPHABET.index(key):
            result[j + 1] = result[j]   # shift the bigger letter to the right
            j -= 1
        result[j + 1] = key
    return result


if __name__ == "__main__":
    unsorted_array = build_unsorted(full_name)
    sorted_array = insertion_sort(unsorted_array)

    print("Full Name:", full_name)
    print("Unsorted array:", unsorted_array)
    print("Sorted array:  ", sorted_array)

def isValidSubsequence(array, sequence):
    # Write your code here.
    seq_index = 0
    for i in array:
        print(f"Comparin {i} with {sequence[seq_index]}")
        if i == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    # print(seq_index)
    # print(len(sequence))
    return False

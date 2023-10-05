def get_all_subsequences_recursive(A: list):
    '''Recursive method
    '''
    if len(A) <= 1:
        return [[], A]
    elif len(A) == 2:
        return [[], [A[0]], [A[1]], A]
    else:
        subseqs = get_all_subsequences_recursive(A[1:])
        subseqs = subseqs + [ [A[0]] ] + [ [A[0]] + subseq for subseq in subseqs ]
        return subseqs


def get_all_subsequences(A: list):
    '''Iterative method
    '''
    subseqs = [[]]
    for element in A:
        additional_subseqs = []
        for subseq in subseqs:
            if subseq:
                additional_subseqs.append(subseq + [element])
        subseqs.append([element])
        subseqs += additional_subseqs
    return subseqs


def get_all_increasing_subsequences_recursive(A: list):
    '''Recursive method
    '''
    if len(A) <= 1:
        return [[], A]
    elif len(A) == 2:
        if A[0] < A[1]:
            return [[], [A[0]], [A[1]], A]
        else:
            return [[], [A[1]], [A[0]]]
    else:
        subseqs = get_all_increasing_subsequences_recursive(A[1:])
        subseqs = subseqs \
            + [ [A[0]] ] \
            + [ [A[0]] + subseq for subseq in subseqs if subseq and A[0] < subseq[0] ]
        return subseqs


def get_all_increasing_subsequences(A: list):
    '''Iterative method
    '''
    subseqs = [[]]
    for element in A:
        additional_subseqs = []
        for subseq in subseqs:
            if subseq and element > subseq[-1]:
                additional_subseqs.append(subseq + [element])
        subseqs.append([element])
        subseqs += additional_subseqs
    return subseqs


if __name__ == "__main__":
    test_list = [5,5]
    subseqs_recur = get_all_subsequences_recursive(test_list)
    print(f"Subsequences using recursive: {subseqs_recur}")
    subseqs_iter = get_all_subsequences(test_list)
    print(f"Subsequences using iterative: {subseqs_iter}")
    incr_subseqs_recur = get_all_increasing_subsequences_recursive(test_list)
    print(f"Increasing subsequences using recursive: {incr_subseqs_recur}")
    incr_subseqs_iter = get_all_increasing_subsequences(test_list)
    print(f"Increasing subsequences using iterative: {incr_subseqs_iter}")

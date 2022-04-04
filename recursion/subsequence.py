def get_subsequence(A: list):
    if len(A) == 1:
        print(A)
        return A
    elif len(A) == 2:
        print([A[0]])
        print([A[1]])
        print(A)
        return [[A[0]], [A[1]], A]
    else:
        print(f"Getting subseq for {A[1:]}")
        subseqs = get_subsequence(A[1:])
        to_append = [ [A[0]] + subseq for subseq in subseqs ]
        subseqs = [ [A[0]] ] + subseqs + to_append
        print(f"Here is the result: {subseqs}")
        return subseqs


if __name__ == "__main__":
    subseqs = get_subsequence([1,2,3])
    print(f"Subsequences: {subseqs}")

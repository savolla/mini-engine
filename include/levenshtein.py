def levenshtein(word0, word1):
    matrix = []

    for i in range(len(word0)+1):
        w_append = []
        for j in range(len(word1)+1):
            w_append.append(0)
        matrix.append(w_append)

    for i in range(len(matrix[0])):
        matrix[0][i] = i

    for i in range(len(matrix)):
        matrix[i][0] = i

    for i in range(len(word0)):
        for j in range(len(word1)):
            if word0[i] == word1[j]:
                matrix[i+1][j+1] = matrix[i][j]
            else:
                matrix[i+1][j+1] = min([matrix[i][j], matrix[i][j+1], matrix[i+1][j]])+1

    return matrix[-1][-1]

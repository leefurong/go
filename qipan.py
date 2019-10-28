def createEmptyRow(size):
    return [0] * size


def createEmpty(size=19):
    qipan = []
    for i in range(size):
        newRow = createEmptyRow(size)
        qipan.append(newRow)
    return qipan

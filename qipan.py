def createEmptyRow():
    return [0] * 19


def createEmpty():
    qipan = []
    for i in range(19):
        newRow = createEmptyRow()
        qipan.append(newRow)
    return qipan

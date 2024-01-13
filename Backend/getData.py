def getListCamry():
    dict = []
    with open('toyota_camry.txt', 'r') as f:
        for line in f:
            line=line.strip()
            line=line.lower()
            dict.append(line)
    return dict
from luis_api import *

filesPath = ["Audios/transcript/capex.txt", "Audios/transcript/gog.txt", "Audios/transcript/marcos_criticos.txt", "Audios/transcript/obrigacao.txt"]
types = ["capex", "gog", "marcos_criticos", "obrigacao"]

matrix = []
listinha = []

for idx in range(0,4):
    matrix = []
    listinha = []
    file = open(filesPath[idx], 'r')
    for line in file:
        if len(listinha) == 50:
            matrix.append(listinha)
            listinha = []
        listinha.append({
            "text": line,
            "intentName": types[idx]
        })
    if len(listinha) != 0:
        matrix.append(listinha)
    for coisinha in matrix:
        print(postMsg(coisinha))
    
    print("Lista {} Concluida".format(idx))
    file.close()
    matrix = []
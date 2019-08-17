from luis_api import *

filesPath = ["Audios/transcript/capex.txt", "Audios/transcript/gog.txt", "Audios/transcript/marcos_criticos.txt", "Audios/transcript/obrigacao.txt"]
types = ["capex", "gog", "marcos_criticos", "obrigacao"]

for idx in range(0,3):
    file = open(filesPath[idx], 'r')
    for line in file:
        print(postMsg(line, types[idx]))
    print("Lista {} Concluida".format(idx))
    file.close()
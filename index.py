from gui import *
from speech_to_text import *
from luis_api import *
from utils import *
import os

def cleanScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

exit = False

while exit == False:
    printMainMenu()
    option = input()
    cleanScreen()
    
    if option == "1":
        printVoice()
        text = hearVoice()
        if text != "":
            cleanScreen()
            print("Você disse: {}".format(text))
            print("\n\nSaída: {}\n\n".format(formatResponseJson(teste_exaple(text))))
            input("Pressione enter para Continuar...")
        cleanScreen()
    elif option == "2":
        text = input("Digite a frase: ")
        if text != "":
            print("\n\nSaída: {}\n\n".format(formatResponseJson(teste_exaple(text))))
            input("Pressione enter para Continuar...")
        cleanScreen()
    elif option == "0":
        exit = True
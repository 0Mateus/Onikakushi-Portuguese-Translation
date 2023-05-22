from deep_translator import GoogleTranslator
import os

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def program():
    global loop
    print("Insira o que deve ser traduzido:")
    text = input("Entrada: ")
    translated = GoogleTranslator(source='auto', target='portuguese').translate(text=text)
    print(translated)
    addToClipBoard(translated)
    if translated == "erro":
        loop = False
    else:
        loop = True

if program(): loop == True

while loop == True:
    program()

else:
    print("Closing...")

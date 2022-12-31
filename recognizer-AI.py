import speech_recognition as sr
import re
import os

def listen_microphone():
    # Enable microphone
    microphone = sr.Recognizer()

    # Using microphone
    with sr.Microphone() as source:

        # Reduces ambient noise
        microphone.adjust_for_ambient_noise(source)

        print("\nOlá, diga como posso te ajudar?\n")

        # Stores the audio
        audio = microphone.listen(source)
    try:

        # Uses speech pattern recognizer for brazilian language
        phrase = microphone.recognize_google(audio, language='pt-BR')
        phrase = phrase.lower()

        ##---------- Action options ----------##

        if "abrir navegador" in phrase:
            os.system("start chrome.exe")

        elif "qual a previsão do tempo" in phrase:
            os.system("start chrome.exe www.google.com/search?q=previsão+do+tempo")

        elif "abrir tradutor" in phrase:
            os.system("start chrome.exe https://translate.google.com.br/")

        elif "abrir excel" in phrase:
            os.system("start excel.exe")

        elif "abrir bloco de notas" in phrase:
            os.system("start notepad.exe")

        elif "abrir gerenciador de arquivos" in phrase:
            os.system("start explorer.exe")

        elif "abrir terminal" in phrase:
            os.system("start")

        elif "o que é" in phrase:
            with sr.Microphone() as query:
                microphone.adjust_for_ambient_noise(query)
                print("O que deseja pesquisar?")
                search_query = microphone.listen(query)
                try:
                    phrase = microphone.recognize_google(search_query, language='pt-BR')
                    search = re.sub("o que é ","", phrase)
                    search = '+'.join(search.split(' '))
                    os.system(f"start Chrome.exe www.google.com/search?q={search}")

                # If not recognizer print a message
                except sr.UnknownValueError:
                    print('\nDesculpe, não entendi.')

        # Returns the phrase
        print("Você disse: " + phrase)

    # If not recognizer print a message
    except sr.UnknownValueError:
        print('\nDesculpe, não entendi.')

listen_microphone()
import speech_recognition as sr

# Création d'un objet de reconnaissance vocale
r = sr.Recognizer()

# Capture du son à l'aide du micro
with sr.Microphone() as source:
    audio = r.listen(source)

# Conversion du son en texte
try:
    text = r.recognize_google(audio, language='fr-FR')
    print(text)
except sr.UnknownValueError:
    print("Je n'ai pas compris ce que vous avez dit")
except sr.RequestError as e:
    print("Erreur lors de la reconnaissance vocale : {0}".format(e))
import speech_recognition as sr

# Création d'un objet de reconnaissance vocale
r = sr.Recognizer()

# Capture du son à l'aide du micro
with sr.Microphone() as source:
    audio = r.listen(source)

# Conversion du son en texte
try:
    text = r.recognize_google(audio, language='fr-FR')
    print(text)
except sr.UnknownValueError:
    print("Je n'ai pas compris ce que vous avez dit")
except sr.RequestError as e:
    print("Erreur lors de la reconnaissance vocale : {0}".format(e))

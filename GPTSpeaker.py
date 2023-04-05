import speech_recognition
import gtts
import openai
import os

sr = speech_recognition.Recognizer()

file_path = os.path.abspath('openai_api_key.txt')


def search_str():
    with open(file_path, 'r') as file:
        content = file.read()
        if 's' in content:
            print("Starting programm...")
        else:
            print("Welcome to GPTSpeaker! In this program you can use voice input to communicate with the GPT-3.5 neural network.")
            openai_key = input("Paste your OpenAI API key: ")
            open('openai_api_key.txt', 'w').write(openai_key)


search_str()

while True:
    try:
        print("Speak!")
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='en-US').lower()
        print("User: " + query)

        openai.api_key = open('openai_api_key.txt', 'r').read()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ]
        )
        respi = response['choices'][0]['message']['content']
        print("GPT: " + respi)
        from playsound import playsound

        t1 = gtts.gTTS(respi)
        t1.save("Neuralnetworkresponse.mp3")
        playsound("Neuralnetworkresponse.mp3")
        os.remove("Neuralnetworkresponse.mp3")
        if query == 'bye':
            break
        elif query == 'goodbye':
            break
        else:
            continue
    except speech_recognition.UnknownValueError:
        print("An error occured. Please try again.")

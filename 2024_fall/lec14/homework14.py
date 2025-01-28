import datetime
import gtts
import random
import speech_recognition
import requests
from bs4 import BeautifulSoup

def what_time_is_it(lang, filename):
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    
    tts = gtts.gTTS(f"现在是 {time_str}", lang=lang)
    tts.save(filename)

def tell_me_a_joke(lang, audiofile):
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(joke_url)
    joke = response.json()
    joke_text = f"{joke['setup']} {joke['punchline']}"
    
    tts = gtts.gTTS(joke_text, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    now = datetime.datetime.now()
    day_str = now.strftime("%A, %B %d, %Y")
    
    tts = gtts.gTTS(f"今天是 {day_str}", lang=lang)
    tts.save(audiofile)
    
    current_month = now.strftime("%m")
    current_year = now.year
    url = f"https://www.timeanddate.com/calendar/?year={current_year}&month={current_month}"
    return url

def personal_assistant(lang, filename):
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("正在听，请说话...")
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio, language=lang).lower()
        if "time" in command:
            what_time_is_it(lang, filename)
            print("时间已保存到音频文件中。")
        elif "day" in command:
            url = what_day_is_it(lang, filename)
            print(f"日期已保存到音频文件中，可查看日历链接：{url}")
        elif "joke" in command:
            tell_me_a_joke(lang, filename)
            print("笑话已保存到音频文件中。")
        else:
            print("抱歉，我没有听懂您的请求。")
    except Exception as e:
        print(f"发生错误：{e}")

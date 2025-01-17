import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            print("正在处理音频文件...")
            audio_data = recognizer.record(source)
            print("正在识别音频...")
            text = recognizer.recognize_google(audio_data, language=language)
            return text
    except sr.UnknownValueError:
        return "无法识别音频内容。"
    except sr.RequestError as e:
        return f"服务请求失败: {e}"
    except FileNotFoundError:
        return "找不到指定的音频文件。"

if __name__ == "__main__":
    print("请输入音频文件路径（）：")
    audio_file = input().strip()
    print("请输入语言代码（）：")
    language_code = input().strip() or "en"

    print("开始转录...")
    transcription = transcribe_wavefile(audio_file, language=language_code)
    print("\n转录结果：")
    print(transcription)
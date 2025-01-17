import gtts

def synthesize(text, lang, filename):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"语音合成完成，已保存到文件: {filename}")
    except Exception as e:
        print(f"语音合成失败: {e}")
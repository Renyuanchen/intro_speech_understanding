import bs4
from gtts import gTTS

def extract_stories_from_NPR_text(text):

    soup = bs4.BeautifulSoup(text, 'html.parser')

    stories = []
    for item in soup.find_all('article'):
        title = item.find('h2')
        teaser = item.find('p')

        title_text = title.get_text(strip=True) if title else ''
        teaser_text = teaser.get_text(strip=True) if teaser else ''

        stories.append((title_text, teaser_text))
    
    return stories

def read_nth_story(stories, n, filename):
  
    if n < 0 or n >= len(stories):
        print("无效的索引，无法读取故事。")
        return

    title, teaser = stories[n]
    text_to_synthesize = f"Title: {title}. Teaser: {teaser}"

    try:
        tts = gTTS(text=text_to_synthesize, lang='en')
        tts.save(filename)
        print(f"语音合成完成，保存为文件: {filename}")
    except Exception as e:
        print(f"语音合成失败: {e}")


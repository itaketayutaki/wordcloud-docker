from wordcloud import WordCloud
from sudachipy import dictionary

textList = ["私は猫です", "あなたは犬です", "名状しがたき超自然存在を卑近なる人類が視覚的に認識することは不可能"]
n = 100
textListChunk = [textList[idx:idx + n] for idx in range(0, len(textList), n)]

tokenizer_obj = dictionary.Dictionary().create()
words = []
for textListBatch in textListChunk:
    text = "\n".join(textListBatch)
    morphemes = tokenizer_obj.tokenize(text)
    words = words + [m.normalized_form() for m in morphemes if m.part_of_speech()[0] in ["名詞", "形容詞"]]
wc = WordCloud(
        width=1080,
        height=1920,
        background_color="white",
        stopwords={"もの","これ","ため","それ","ところ","よう","こと","人","時","方","気","今","奴","無い"}, 
        font_path="/usr/share/fonts/static/NotoSansJP-Bold.ttf",
        max_words=100,
        collocations=False
    )
wc.generate(" ".join(words))
wc.to_file('wordcloud.png')
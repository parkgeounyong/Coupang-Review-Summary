import openai
import re
from konlpy.tag import Okt
from nltk import Text
import matplotlib.pyplot as plt

openai.api_key = "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"


def Tokenizer(text):
    okt = Okt()

    # 형태소 분석
    morphemes = okt.pos(text)

    # 명사, 형용사 형태소만 추출
    adj = [word for word, pos in morphemes if pos in ['Adjective'] and len(word) >= 2 and word not in ['입니다', '있습니다']]

    # 단어 빈도수 계산
    adj_freq = Text(adj).vocab()

    # 빈도수가 높은 단어 10개 출력
    top_adj = adj_freq.most_common(10)
    #top_nouns = [t[0] for t in top_nouns]
    top_adj = [t[0] for t in top_adj]
    # 결과 출력
    return top_adj

    

def extract_element(text):
    # 문장 요약
    prompt = "! 이후 단어는 고기 상품에 대한 후기들의 반응들이야. 이를 기반으로 고기 상품의 후기를 간단하게 작성해줘\n!"
    top_adj = Tokenizer(text)
    prompt+="\n형용사: "
    for token in top_adj:
        prompt += token+" "
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=10,
        stop=None,
        temperature=0.8,
    )
    message = completions.choices[0].text.strip()
    return message


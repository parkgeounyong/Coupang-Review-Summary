from src.crawl import OpenPyXL
from src.openai_method import *
import os
import json

#쿺팡에서 돼지고기 리뷰를 크롤링하여 토큰화
#prompt:prompt내용+토큰, comploetion: 리뷰로 fine turning데이터 준비
if __name__ == '__main__':
    review_collection=OpenPyXL.save_file()

    with open("fine_truning/metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    #metadata = []
    
    for text in review_collection:
        adjective_group=Tokenizer(text)
        if len(adjective_group)!=0:
            metadata.append({"prompt": "다음 형용사들은 다수의 돼지 고기 리뷰에서 추출된 형용사들이야. 해당 형용사들을 기반으로 간단한 리뷰를 작성해줘\n"
                +str(adjective_group).strip('[]'), "completion": text})

    # 메타데이터 파일 저장
    with open("fine_truning/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=1)

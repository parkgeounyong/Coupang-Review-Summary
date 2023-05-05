from src.crawl import OpenPyXL
from src.openai_method import *
import os
import json

#쿺팡에서 돼지고기 리뷰를 크롤링하여 토큰화
if __name__ == '__main__':
    review_collection=OpenPyXL.save_file()

    #with open("fine_truning/Adjective_Analysis.json", "r", encoding="utf-8") as f:
    #    metadata = json.load(f)
    dict = {}
    
    for text in review_collection:
        adjective_group=Tokenizer(text)
        dict.update(adjective_group)

    with open("fine_truning/Adjective_Analysis.json", "w", encoding="utf-8") as f:
        json.dump(dict, f, ensure_ascii=False, indent=1)

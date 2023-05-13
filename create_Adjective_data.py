from src.crawl import OpenPyXL
from src.crawl import Coupang
from src.openai_method import *
import os
import json

#입력으로 해당 카테고리에 가장 첫 페이지 입력 필요
if __name__ == '__main__':

    
    full_url=Coupang.input_review_url()
    print(Coupang.fullPage(full_url))
    for i in range(2,18):
        print(full_url+"?page="+str(i))
        print(Coupang.fullPage(full_url+"?page="+str(i)))

    #review_collection=OpenPyXL.save_file()

    #with open("fine_truning/Adjective_Analysis.json", "r", encoding="utf-8") as f:
    #    dict = json.load(f)
    #dict = {}
    
    #for text in review_collection:
    #    adjective_group=Tokenizer(text)
    #    dict.update(adjective_group)

    #with open("fine_truning/Adjective_Analysis.json", "w", encoding="utf-8") as f:
    #    json.dump(dict, f, ensure_ascii=False, indent=1)

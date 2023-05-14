from src.crawl import OpenPyXL
from src.crawl import Coupang
from src.openai_method import *
import os
import json

#입력으로 해당 카테고리에 가장 첫 페이지 입력 필요
if __name__ == '__main__':

    baby_product_links=[]
    full_url=Coupang.input_review_url()
    for baby_product_link in Coupang.fullPage(full_url):
        baby_product_links.append(baby_product_link)
    for i in range(2,18):
        for baby_product_link in Coupang.fullPage(full_url+"?page="+str(i)):
            baby_product_links.append(baby_product_link)
  
    dict=[]
    for baby_product_link in baby_product_links:
        print("https://www.coupang.com"+baby_product_link)
        review_collection=OpenPyXL.save_file("https://www.coupang.com"+baby_product_link)
        for text in review_collection:
            #adjective_group=Tokenizer(text)
            #dict.update(adjective_group)
            dict.append(text)
            print(text)
            with open("fine_truning/Adjective_Analysis.json", "w", encoding="utf-8") as f:
                json.dump(dict, f, ensure_ascii=False, indent=1)
    print(dict)
    


    with open("fine_truning/Adjective_Analysis.json", "w", encoding="utf-8") as f:
        json.dump(dict, f, ensure_ascii=False, indent=1)

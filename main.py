from src.crawl import OpenPyXL
from src.openai_method import extract_element

if __name__ == '__main__':
    review_collection=OpenPyXL.save_file()
    element=extract_element(review_collection[0]+"\n"+"위의 문장에서 중요한 단어를 추출하여 ,으로 구분해줘")
    
    print(review_collection[0])
    print(element)
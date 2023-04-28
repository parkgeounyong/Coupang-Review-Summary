from src.crawl import OpenPyXL
from src.openai_method import *

if __name__ == '__main__':
    review_collection=OpenPyXL.save_file()

    text=""
    for review in review_collection:
        text=text+review
        
    element=extract_element(text)
    print(element)
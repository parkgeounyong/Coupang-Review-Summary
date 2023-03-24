from src.crawl import OpenPyXL

if __name__ == '__main__':
    review_collection=OpenPyXL.save_file()
    
print(review_collection)
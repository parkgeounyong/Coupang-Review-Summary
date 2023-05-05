#각 파일별 설명
1. main.py
입력: 쿠팡 url
출력: 해당 쿠팡 url 후기 요약문

2. create_train_data.py
입력: 쿠팡 url
출력: 각 후기별 fine tuning data 생성(metadata.json)

3. create_Adjective_data.py
입력: 쿠팡 url
출력: 크롤링한 전체 후기 형용사 딕셔너리(형용사: 출현 횟수)(Adjective_Analysis.json)
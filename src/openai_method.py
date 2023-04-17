import openai
openai.api_key = "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"

def extract_element(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text+"\n"+"위의 문장에서 상품에만 해당하는 필수적인 요소를 추출해줘",
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.5,
        presence_penalty=0,
        frequency_penalty=0
    )
    result = response.choices[0].text.strip()
    if result == "":
        return []
    else:
        return result.split(" ")




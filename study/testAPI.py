import openai

# OpenAI API 키 설정
api_key = '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'
openai.api_key = api_key

def get_openai_response(prompt):
    # OpenAI API를 통해 대화형 답변 얻기
    response = openai.Completion.create(
        engine="text-davinci-003",  # 적절한 엔진 선택 (GPT-3.5는 아직 새로운 엔진 이름으로 제공되지 않습니다)
        prompt=prompt,
        max_tokens=1000  # 적절한 값 선택 (원하는 만큼 크게 조정)
    )
    
    # API 응답에서 전체 답변 추출
    answer = response['choices'][0]['text']
    return answer

def main():
    # 사용자로부터 질문 입력 받기
    prompt = input("질문을 입력하세요: ")

    # OpenAI API에 질문 전송하고 전체 답변 얻기
    answer = get_openai_response(prompt)

    # 전체 답변 출력
    print("답변:", answer)

if __name__ == "__main__":
    main()

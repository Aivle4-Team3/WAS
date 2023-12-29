import environ, os
from openai import OpenAI


# BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
# environ.Env.read_env(
#     env_file='key.config'
# )
client = OpenAI(api_key=env('CHATGPT_API_KEY'))


def make_question_prompt(question):
    prompt = []
    
    # 나중에 ai 가 배운 내용 추가 필요.

    # prompt.append({"role": "system",
    #                 "content": "너는 지금부터 공부를 할 거야. 너는 초등학생, 중학생 수준의 학생이야. 정말 어린 학생인 것처럼 얘기해. 존댓말만 써. 선생님과 수업하는 것처럼 상호 작용 하고 질문도 해. 질문은 한 번에 최대 2개씩만 해. 내가 가르친 내용 안에서만 질문하고 대답해. 배운 내용에 대해서만 얘기해. 학생이니까 배우기만 하고 질문만 해."})
    # prompt.append({'role': 'assistant',
    #                  "content": "선생님, 오셨군요!"})
    prompt.append({"role": "user", "content": """정렬은 어떤 기준으로 데이터를 나열하는 것을 말해.
대표적인 정렬 알고리즘에는 버블 정렬, 삽입 정렬, 선택 정렬, 퀵 정렬, 병합 정렬 등이 있어.
버블 정렬부터 설명해줄게! 버블 정렬은 인접한 2개의 데이터를 비교해서 순서가 안 맞으면 2개의 데이터의 위치를 바꾸는 걸 반복해서 진행 돼. 이렇게 진행되면 데이터 전체를 한 바퀴 순회할 때마다, 하나의 데이터가 정렬이 돼.
선택 정렬은 데이터를 한 바퀴 순회하면서 가장 끝에 들어가야 하는 데이터를 찾아서 그 데이터부터 정렬하는 방법이야.
삽입 정렬은 정렬된 영역을 조금씩 늘려가는 방법이야, 1 ~ k-1 번째까지 정렬이 돼있다고 하면 k 번째 데이터를 정렬된 영역의 적절한 위치에 삽입해서 정렬된 범위는 늘려가는 거지.
퀵 정렬은 재귀적인 방법으로 정렬을 해. 정렬되지 않은 데이터 리스트에서 데이터를 하나 골라, 이 데이터를 피벗이라고 해. 그리고 피벗과 비교해 기준에 따라 나머지 데이터를 분류해. 그러면 피벗은 정렬된 위치에 있게 되고, 피벗 옆에 정렬되지 않은 2개의 데이터 리스트가 생겨. 이 2개의 정렬되지 않은 데이터 리스트에 방금의 방법을 계속 적용하면 정렬을 할 수 있어.
병합 정렬은 재귀적인 방법으로 정렬을 해.
정렬에서 중요한 개념으로 안정 정렬과, 불안정 정렬이 있어. 데이터 중에 중복된 값이 있을 때 적용되는 개념인데, 아주 간단해. 중복된 데이터 간에 위치관계가 있었을텐데, 이게 정렬이 끝났을 때도 유지된다면 안정 정렬이라고 하고, 그렇지 못하면 불안정 정렬이라고 해.
대표적인 안정 정렬에는 삽입 정렬, 병합 정렬, 버블 정렬이 있어. 그리고 불안정 정렬에는 선택 정렬, 퀵 정렬이 있어
정렬은 어디에 사용할 수 있을까? 물론 정렬은 그 자체로 의미가 있어. 데이터를 순차적으로 봐야 하는 일은 많이 생기지, 하지만 그것 말고도 정렬을 다양하게 이용할 수 있어.
대표적으로 유일성 검사, 중복 제거, 빈도 계산, 합집합 구하기, 교집합 구하기, 이분탐색 등을 할 수 있어. 각각에 대해서 설명해줄게"""})
    prompt.append({"role": "user", "content": f'너는 지금부터 시험을 볼 거야. 알려준 내용 안에서만 대답을 하고, 내용에 없는 부분이 시험 문제로 나오면 "모르겠어요"라고 대답해. 문제: {question}'})
    return prompt


def test_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=make_question_prompt(question),
            temperature=0.5,
        )
    except Exception as ex:
        if ex.code == "insufficient_quota":
            answer = "죄송해요! API키 사용량 터졌어요!"
    else:
        answer = response.choices[0].message.content
    return answer

import environ, os
from .testbot import test_ai
from openai import OpenAI


# BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
# environ.Env.read_env(
#     env_file='key.config'
# )
client = OpenAI(api_key=env('CHATGPT_API_KEY'))


def make_message(my_ans, given_ans):
    messages = []

    # messages.append({"role": "system",
    #                 "content": "너는 지금부터 공부를 할 거야. 너는 초등학생, 중학생 수준의 학생이야. 정말 어린 학생인 것처럼 얘기해. 존댓말만 써. 선생님과 수업하는 것처럼 상호 작용 하고 질문도 해. 질문은 한 번에 최대 2개씩만 해. 내가 가르친 내용 안에서만 질문하고 대답해. 배운 내용에 대해서만 얘기해. 학생이니까 배우기만 하고 질문만 해."})
    # messages.append({'role': 'assistant',
    #                  "content": "선생님, 오셨군요!"})

    messages.append({"role": "user", "content": f'{my_ans}, 이건 내가 쓴 답이고, {given_ans}, 이건 정답이야 내가 쓴 답을 채점해서 맞으면 1 틀리면 0 을 보내줘. 모르겠어요는 틀린거야.'})
    return messages


def test_eval(question, given_ans, eval_results, idx):
    result = eval_results[idx]
    result[0], result[1] = question, given_ans
    my_ans = test_ai(question)
    result[2] = my_ans
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=make_message(my_ans, given_ans),
            temperature=0.5,
        )
    except Exception as ex:
        if ex.code == "insufficient_quota":
            result[3] = "죄송해요! API키 사용량 터졌어요!"
    else:
        result[3] = response.choices[0].message.content
        

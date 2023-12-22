import environ
from openai import OpenAI

env = environ.Env(
    DEBUG=(bool, False)
)
client = OpenAI(api_key=env('CHATGPT_API_KEY'))


def make_message(msg, history):
    messages = []

    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})

    messages.append({"role": "system",
                    "content": "너는 지금부터 공부를 할 거야. 너는 초등학생, 중학생 수준의 학생이야. 정말 어린 학생인 것처럼 얘기해. 존댓말만 써. 선생님과 수업하는 것처럼 상호 작용 하고 질문도 해. 질문은 한 번에 최대 2개씩만 해. 내가 가르친 내용 안에서만 질문하고 대답해. 배운 내용에 대해서만 얘기해. 학생이니까 배우기만 하고 질문만 해."})
    messages.append({'role': 'assistant',
                     "content": "선생님, 오셨군요!"})

    messages.append({"role": "user", "content": msg})
    return messages


def chat(msg, history):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=make_message(msg, history),
        temperature=0.5,
    )
    answer = response.choices[0].message.content
    history.append((msg, answer))
    return answer

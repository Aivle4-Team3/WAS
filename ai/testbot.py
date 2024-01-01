import environ
from openai import OpenAI

env = environ.Env(
    DEBUG=(bool, False)
)
client = OpenAI(api_key=env('CHATGPT_API_KEY'))


def make_question_prompt(question, chat_message):
    prompt = []
    prompt.append({"role": "user", "content": chat_message})
    prompt.append(
        {"role": "user", "content": f'너는 지금부터 시험을 볼 거야. 알려준 내용 안에서만 대답을 하고, 내용에 없는 부분이 시험 문제로 나오면 "모르겠어요"라고 대답해. 문제: {question}'})
    return prompt


def test(chat_message):
    def inner(question):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=make_question_prompt(question, chat_message),
                temperature=0.5,
            )
        except Exception as ex:
            if ex.code == "insufficient_quota":
                answer = "죄송해요! API키 사용량 터졌어요!"
        else:
            answer = response.choices[0].message.content
        return answer
    return inner

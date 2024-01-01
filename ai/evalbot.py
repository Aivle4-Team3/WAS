import environ
from openai import OpenAI

env = environ.Env(
    DEBUG=(bool, False)
)
client = OpenAI(api_key=env('CHATGPT_API_KEY'))


def make_message(my_ans, given_ans):
    messages = []

    messages.append(
        {"role": "user", "content": f'{my_ans}, 이건 내가 쓴 답이고, {given_ans}, 이건 정답이야 내가 쓴 답을 채점해서 맞으면 1 틀리면 0 을 보내줘. 모르는건 틀린거야.'})
    return messages


def test_eval(question, answer, test, result):
    try:
        test_paper = test(question)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=make_message(test_paper, answer),
            temperature=0.5,
        )
    except Exception as ex:
        test_paper = ""

        if ex.code == "insufficient_quota":
            evaluation = "죄송해요! API키 사용량 터졌어요!"
        else:
            evaluation = ex.code
    else:
        evaluation = response.choices[0].message.content

    result[:] = (question, answer, test_paper, evaluation)

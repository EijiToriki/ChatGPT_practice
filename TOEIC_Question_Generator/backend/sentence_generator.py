## 参考：https://www.a-c-japan.com/solution/chatgpt/chatgpt-api/
import openai

openai.api_key = ""

# ------------------------------------------------------------
# チャットボットを呼び出す関数を設定
# ------------------------------------------------------------

def ans_ChatGPT(question):
    # ChatGPT に質問内容を送信し、応答を取得するメソッド
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",    # ChatGPT のモデル選択
        messages=[{
          "role": "user",         # ユーザの発話であることを示す
          "content": question,    # 質問内容を入れる変数
        }]
    )

    # 質問に対する回答
    res = completion.choices[0].message.content
    
    return res


# ChatGPTより得られる英文を整形して提供する関数
def sentences_provider():
    question = "TOEICのpart5で出題されそうな英文を3つ作って"
    res = ans_ChatGPT(question)

    res = res.split('\n')

    sentences = []
    for sent in res:
        if len(sent) == len(sent.encode('utf-8')) and len(sent) > 10:
            sentences.append(sent)
    
    return sentences


if __name__ == '__main__':
    print(sentences_provider())
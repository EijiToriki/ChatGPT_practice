## 参考：https://www.a-c-japan.com/solution/chatgpt/chatgpt-api/
import openai
from nltk.tokenize import sent_tokenize

openai.api_key = "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"

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
    for sents in res:
        if len(sents) == len(sents.encode('utf-8')) and len(sents) > 10:
            sents = sents[3:]   # 1. の除去
            sents = sent_tokenize(sents)
            for sent in sents:
                sentences.append(sent)
    
    return sentences


if __name__ == '__main__':
    print(sentences_provider())

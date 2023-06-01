import nltk
import sqlite3

## chatGPTで文が作られるたびに、形態素解析を行い、新規単語を格納する


def connenct_DB():
  dbname = 'TOEIC_ChatGPT.db'
  conn = sqlite3.connect(dbname)

  return conn


# DBへの単語挿入
def insert_word(sentences):
  conn = connenct_DB()
  # sqliteを操作するカーソルオブジェクトを作成
  cur = conn.cursor()

  # 文を形態素解析して、品詞ごとに格納する
  for sentence in sentences:
    words = nltk.word_tokenize(sentence)  # 単語分割
    wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形
    for wp in wps:
        w = wp[0]   # 単語
        p = wp[1]   # 品詞

        # cur.execute("insert into part5_words(word, pos) values (:word, :pos);", {"word": w, "pos": p})


  cur.close()
  conn.commit()
  conn.close()



## part5_sentences から文を全文取得する（初回実行のみ）
def extract_sentence():
  conn = connenct_DB()
  cur = conn.cursor()

  cur.execute('select sentences from part5_sentences')
  res = cur.fetchall()

  ## リストに現在入っている文を格納する
  sentences = []
  for i in range(len(res)):
    sentences.append(res[i][0])

  cur.close()
  conn.commit()
  conn.close()

  return sentences


if __name__ == '__main__':
  sentence_list = [
      "I have played tennis for ten years .",
      "He has lived in New York since 1999 .",
      "She had left before I got there .",
      "The building was built in 1990 .",
      "The wooden desk is made by Sherry .",      
    ]
  insert_word(sentence_list)
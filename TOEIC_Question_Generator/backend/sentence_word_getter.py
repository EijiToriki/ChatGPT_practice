##################################################
## 文章テーブル、単語テーブルよりデータ抽出する
##################################################
import sqlite3

def connenct_DB():
  dbname = 'TOEIC_ChatGPT.db'
  conn = sqlite3.connect(dbname)

  return conn


## DBから問題数分 文を取得する
def extract_sentence(n):
  conn = connenct_DB()
  cur = conn.cursor()

  cur.execute('select * from part5_sentences where is_used = 0 limit :n',{"n": n})
  res = cur.fetchall()

  ## 使用済みフラグを立てる
  for i in range(n):
    cur.execute('update part5_sentences set is_used = 1 where id = :id',{"id": res[i][0]})

  cur.close()
  conn.commit()
  conn.close()

  return res


## part5_words から問題の答えと同じ品詞の単語を3つ取り出す
def extract_words(ans_pos):
  conn = connenct_DB()
  cur = conn.cursor()

  cur.execute('select sentences from part5_words where pos = :pos',{"pos": ans_pos })
  res = cur.fetchall()

  # sentences = []
  # for i in range(len(res)):
  #   sentences.append(res[i][0])

  cur.close()
  conn.commit()
  conn.close()

  return None


if __name__ == '__main__':
  sentence_list = [
      "I have played tennis for ten years .",
      "He has lived in New York since 1999 .",
      "She had left before I got there .",
      "The building was built in 1990 .",
      "The wooden desk is made by Sherry .",      
    ]
  
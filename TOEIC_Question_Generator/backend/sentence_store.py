import sqlite3
from sentence_generator import sentences_provider

## DBのコネクション
def connenct_DB():
  dbname = 'TOEIC_ChatGPT.db'
  conn = sqlite3.connect(dbname)

  return conn


## DBへの挿入
def insert_sentence(conn, sentence_list):
  # sqliteを操作するカーソルオブジェクトを作成
  cur = conn.cursor()

  for sentence in sentence_list:
    cur.execute("insert into part5_sentences(sentences, is_used) values (:sentence, 0);", {"sentence": sentence})

  cur.close()
  conn.commit()
  conn.close()


## chatGPTで作った文をDBに溜める
def store_DB():
  # 英文リストの取得
  sentence_list = sentences_provider()
  
  # DB接続
  conn = connenct_DB()
  
  # 英文リストをDBに挿入
  insert_sentence(conn, sentence_list)

  return sentence_list


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




if __name__ == '__main__':
  # store_DB()
  print(extract_sentence(2))
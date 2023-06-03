##################################################
## 文章テーブル、単語テーブルにデータを挿入する
##################################################
import time
import nltk
import schedule

import sqlite3
from sentence_generator import sentences_provider

## DBのコネクション
def connenct_DB():
  dbname = 'TOEIC_ChatGPT.db'
  conn = sqlite3.connect(dbname)

  return conn


## DBへの文章挿入
def insert_sentence(conn, sentence_list):
  # sqliteを操作するカーソルオブジェクトを作成
  cur = conn.cursor()

  for sentence in sentence_list:
    cur.execute("insert into part5_sentences(sentences, is_used) values (:sentence, 0);", {"sentence": sentence})
  
  cur.close()


# DBへの単語挿入
def insert_word(conn, sentence_list):
  # sqliteを操作するカーソルオブジェクトを作成
  cur = conn.cursor()

  # 文を形態素解析して、品詞ごとに格納する
  ## 格納しない品詞の集合
  black_list = set(
    ('CD', 'DT', 'EX', 'FW', 'LS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB')
  )

  for sentence in sentence_list:
    words = nltk.word_tokenize(sentence)  # 単語分割
    wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形
    for wp in wps:
        w = wp[0]   # 単語
        p = wp[1]   # 品詞

        if p not in black_list and len(w) > 1:
          try:
            cur.execute("insert into part5_words(word, pos) values (:word, :pos);", {"word": w, "pos": p})
          except sqlite3.IntegrityError:
            print('{} ({}) は、既にテーブルに格納されています'.format(w, p))

  cur.close()


## chatGPTで作った文および単語をDBに溜める
def store_DB():
  # 英文リストの取得
  sentence_list = sentences_provider()
  print(sentence_list)
  
  # DB接続
  conn = connenct_DB()
  
  # 英文リストを文章用テーブルに挿入
  insert_sentence(conn, sentence_list)

  # 英文リストを形態素解析し、単語用テーブルに挿入
  insert_word(conn, sentence_list)

  conn.commit()
  conn.close()


if __name__ == '__main__':
  schedule.every(20).seconds.do(store_DB)

  while True:
    schedule.run_pending()
    time.sleep(1)
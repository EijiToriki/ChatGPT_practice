import sqlite3

# DBの作成
dbname = 'TOEIC_ChatGPT.db'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# テーブル削除
cur.execute(
    'drop table part5_sentences'
)

cur.execute(
    'drop table part5_words'
)


# テーブル作成
cur.execute(
    'create table part5_sentences(id INTEGER PRIMARY KEY AUTOINCREMENT, sentences TEXT, is_used INTEGER)'
)

cur.execute(
    'create table part5_words(id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT, pos TEXT, unique(word, pos))'
)

# データ挿入
# cur.execute('insert into part5_sentences(sentences, is_used) values ("I like an apple", 0)')
# cur.execute('insert into part5_sentences(sentences, is_used) values ("I like an orange", 0)')

# cur.execute('insert into part5_words(word, pos) values ("like", "V")')
# cur.execute('insert into part5_words(word, pos) values ("like", "V")')
## ユニーク制約でエラー

conn.commit()
conn.close()
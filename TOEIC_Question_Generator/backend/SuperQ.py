# ----------------------------------------
# 問題生成クラスの親クラス
# ----------------------------------------
import nltk

class SuperQ():
    def return_Q_material(self):
        pass
    
    def get_word_pos(self, sentence):
      words = nltk.word_tokenize(sentence)  # 単語分割
      wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形

      return words, wps
    
    def mask_sentence(self):
       pass
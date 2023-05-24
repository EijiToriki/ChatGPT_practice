# ----------------------------------------
# 同じ品詞異なる意味の中から適切な単語を選択する問題を生成する
# ----------------------------------------

import nltk
import random
from sentence_generator import ans_ChatGPT
from collections import defaultdict

class Mean_Q_generator:
    norn_list = ["NN", "NNS"]
    verb_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

    def __init__(self):
        self.q_sentences = []        # 問題文を格納するリスト
        self.ans_words = []          # 答えの単語を格納するリスト
        self.options = []            # 問題の選択肢を格納するリスト


    def return_Q_material(self, sentence_list):
        for sent in sentence_list:
            words, wps = self.get_word_pos(sentence=sent)                      # 単語分割および品詞の取得を行う
            q_sent, ans_word = self.mask_sentence(words, wps)                  # 問題文となる動詞をマスクする。また、答えの単語も取得
            option = self.generate_option(ans_word)                            # 選択肢リストの生成

            ## 1問のワンセット（問題文、答え、選択肢）を追加
            self.q_sentences.append(q_sent)
            self.ans_words.append(ans_word)
            self.options.append(option)

        return self.q_sentences, self.ans_words, self.options


    ## 単語分割および品詞の取得を行う
    def get_word_pos(self, sentence):
        words = nltk.word_tokenize(sentence)  # 単語分割
        wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形

        return words, wps


    ## 問題文とその答えを返す
    def mask_sentence(self, words, wps):
        # 名詞(NN, NNS), 動詞(VB, VBD, VBG, VBN, VBP, VBZ),
        # 形容詞(JJ, JJR, JJS), 副詞(RB)それぞれのインデックスを保持
        pos_dict = defaultdict(list)
        for i, wp in enumerate(wps):
            w = wp[0]   # 単語
            p = wp[1]   # 品詞
            if p in self.norn_list:
              pos_dict['n'].append(i)

        hole_num = random.choice(pos_dict['n'])

        if isinstance(hole_num, int):
            ans_word = words[hole_num]
            words[hole_num] = '<MASK>'
        else:
            ans_word = []
            for n in hole_num:
                ans_word.append(words[n])
            ans_word = ' '.join(ans_word)

            words[hole_num[0]] = '<MASK>'
            for i in range(1, len(hole_num)):
                words.remove(words[hole_num[i]])

        return ' '.join(words), ans_word



    ## 選択肢リストの生成
    def generate_option(self, ans_word):
        error_flag = True
        ### chatGPT の返す答えが、想定外だったら繰り返す
        while error_flag:
            try:
                option = [ans_word]
                question = ans_word + "と意味の異なる単語を3つ教えて"
                res = ans_ChatGPT(question)        # chatGPTに選択肢を作ってもらう
                res = res.split('\n')
        
                for option_word in res:
                    haihun_idx = option_word.index('-')
                    option_word = option_word[3:haihun_idx-1]   # 1._のため3文字目スタート、ハイフン前まで取得で単語を抽出
                    option.append(option_word.lower())
                if len(option) == 4:
                    error_flag = False
                else:
                    error_flag = True
            except ValueError:
                print(res)
                error_flag = True
            
        ## 先頭大文字だった場合の処理
        if ans_word.istitle():
            option = [op.capitalize() for op in option]

        return option
  


if __name__ == '__main__':
    sentence_list = [
      "The IT department is currently working on a software upgrade that will improve the company's network security.",
      "According to the latest sales figures, the company's revenue has increased by 15% compared to the same period last year.",
      "The HR department is organizing a series of training sessions on workplace diversity and inclusion for all employees."
    ]


    VerbQGen = Mean_Q_generator()
    a,b,c = VerbQGen.return_Q_material(sentence_list)
    
    for i,j,k in zip(a,b,c):
        print(i,j,k)
        print()
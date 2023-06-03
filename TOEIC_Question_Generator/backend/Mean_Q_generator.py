# ----------------------------------------
# 同じ品詞異なる意味の中から適切な単語を選択する問題を生成する
# ----------------------------------------

import random
from collections import defaultdict
from sentence_word_getter import extract_words

import SuperQ

class Mean_Q_generator(SuperQ.SuperQ):
    norn_list = ["NN", "NNS"]
    verb_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

    def __init__(self):
        self.q_sentences = []        # 問題文を格納するリスト
        self.ans_words = []          # 答えの単語を格納するリスト
        self.options = []            # 問題の選択肢を格納するリスト


    def return_Q_material(self, sentence_list):
        for sent in sentence_list:
            words, wps = self.get_word_pos(sentence=sent)                      # 単語分割および品詞の取得を行う
            q_sent, ans_word, ans_pos = self.mask_sentence(words, wps)                  # 問題文となる動詞をマスクする。また、答えの単語も取得
            option = self.generate_option(ans_word, ans_pos)                            # 選択肢リストの生成

            ## 1問のワンセット（問題文、答え、選択肢）を追加
            self.q_sentences.append(q_sent)
            self.ans_words.append(ans_word)
            self.options.append(option)

        return self.q_sentences, self.ans_words, self.options


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

        ans_word = words[hole_num]
        ans_pos = wps[hole_num][1]
        words[hole_num] = '<MASK>'
    
        return ' '.join(words), ans_word, ans_pos



    ## 選択肢リストの生成
    def generate_option(self, ans_word, ans_pos):
        print(ans_word, ans_pos)
        option = [ans_word]
        option.extend(
            random.sample(extract_words(ans_word, ans_pos), 3)
        )
                    
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
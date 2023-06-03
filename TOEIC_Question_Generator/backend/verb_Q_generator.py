# ----------------------------------------
# 動詞の活用形を問う問題を生成する
# ----------------------------------------

import random
import mlconjug3

import SuperQ

from nltk.stem import WordNetLemmatizer
from collections import defaultdict


class Verb_Q_generator(SuperQ.SuperQ):
    verb_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
    have_list = ["have", "had", "has"]
    be_list = ["am", "was", "are", "were", "is", "be"]
    speceial_verb = ["run", "become", "come"]   # 原形と過去分詞が同じレアパターン

    def __init__(self):
        self.q_sentences = []        # 問題文を格納するリスト
        self.ans_words = []          # 答えの単語を格納するリスト
        self.options = []            # 問題の選択肢を格納するリスト


    def return_Q_material(self, sentence_list):
        for sent in sentence_list:
            words, wps = self.get_word_pos(sentence=sent)                      # 単語分割および品詞の取得を行う
            q_sent, ans_word = self.mask_sentence(words, wps)                  # 問題文となる動詞をマスクする。また、答えの単語も取得
            base_verb = self.change2base(ans_word)                             # 動詞の原形を取得する
            verb_list = self.get_conjugated_verb_list(base_verb)               # 単語の活用形を取得する
            verb_list = self.add_pp_verb_list(verb_list)                       # 単語の活用形リストに現在完了を追加する
            option = self.generate_option(ans_word, verb_list)                 # 選択肢リストの生成

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
            if p in self.verb_list:
                ## 現在完了であるか判定
                if self.judge_pp(w, wps, i):
                    pos_dict['v'].append((i, i+1))
                ## 受動態であるか判定
                elif self.judge_passive(w, wps, i):
                    pos_dict['v'].append((i, i+1))
                else:
                    pos_dict['v'].append(i)

        hole_num = random.choice(pos_dict['v'])

        ## 現在完了・受動態の場合は、リストとして hole_num に格納されているため判定が必要
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


    ### 現在完了かを判定する
    """ 
    単語 w が have, has, had かを判定
    これら3つのうちどれかであれば、次の単語 wps[idx + 1] が過去分詞かを判定
    2つの条件を満たしたら、現在完了であると判定し true を返す
    """
    def judge_pp(self, w, wps, idx):
        if w in self.have_list:
            try:
                if wps[idx+1][1] == "VBN":
                    return True
            except IndexError:
                return False
        
        return False


    ### 受動態かを判定する
    """
    単語 w が be動詞 かを判定
    これら3つのうちどれかであれば、次の単語 wps[idx + 1] が過去分詞かを判定
    2つの条件を満たしたら、現在完了であると判定し true を返す
    """
    def judge_passive(self, w, wps, idx):
        if w in self.be_list:
            try:
                if wps[idx+1][1] == "VBN":
                    return True
            except IndexError:
                return False
        
        return False


    ## 受け取った動詞を原形に変換する
    def change2base(self, verb_word):
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(verb_word.split()[-1], pos='v')


    ## 動詞の原形から動詞の活用形リストを返す
    def get_conjugated_verb_list(self, base_verb):
        ## mlconjug3 で動詞の活用形リストを取得する
        conjugator = mlconjug3.mlconjug.Conjugator(language='en')
        verb_obj = conjugator.conjugate(base_verb)
        verb_list = verb_obj.iterate()

        ## verb_listから第3要素のみ取得し、重複を削除する
        res = []    
        for verb in verb_list:
            if verb[-1] not in res:
                res.append(verb[-1])
        return res


    ## 動詞の活用形リストに現在完了を追加(pp = present perfect = 現在完了)
    def add_pp_verb_list(self, verb_list):
        if verb_list[0] in self.speceial_verb:
            pp = verb_list[0]
        elif len(verb_list) == 4:
            pp = verb_list[0]
        elif len(verb_list) == 5:
            pp = verb_list[2]
        else:
            pp = verb_list[4]
        
        for have in self.have_list:
            add_have_pp = have + " " + pp
            verb_list.append(add_have_pp)
        
        return verb_list


    ## 選択肢リストの生成
    def generate_option(self, ans_word, verb_list):
        # 選択肢リストの生成
        option = [ans_word]
        
        ## 最初の文字が大文字の場合、選択肢リストも大文字にする
        if ans_word.istitle():
            verb_list = [verb.capitalize() for verb in verb_list]

        ## 諸々のライブラリの精度の問題で、答えがverb_listにない場合がある。
        try:
            verb_list.remove(ans_word)
        except ValueError:
            pass
        option.extend(random.sample(verb_list, 3))
        random.shuffle(option)

        return option


if __name__ == '__main__':
    # sentence_list = [
    #   "The IT department is currently working on a software upgrade that will improve the company's network security.",
    #   "According to the latest sales figures, the company's revenue has increased by 15% compared to the same period last year.",
    #   "The HR department is organizing a series of training sessions on workplace diversity and inclusion for all employees."
    # ]

    sentence_list = [
      "I have played tennis for ten years .",
      "He has lived in New York since 1999 .",
      "She had left before I got there .",
      "The building was built in 1990 .",
      "The wooden desk is made by Sherry .",      
    ]

    VerbQGen = Verb_Q_generator()
    a,b,c = VerbQGen.return_Q_material(sentence_list)
    
    for i,j,k in zip(a,b,c):
        print(i,j,k)
        print()
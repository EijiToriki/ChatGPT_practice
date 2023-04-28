# ----------------------------------------
# 動詞の活用形を問う問題を生成する
# ----------------------------------------

import nltk
import random
import mlconjug3
from nltk.stem import WordNetLemmatizer
from collections import defaultdict


## 単語分割および品詞の取得を行う
def get_word_pos(sentence):
    words = nltk.word_tokenize(sentence)  # 単語分割
    wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形

    return words, wps


## 問題文とその答えを返す
def mask_sentence(words, wps):
    # 名詞(NN, NNS), 動詞(VB, VBD, VBG, VBM, VBP, VBZ),
    # 形容詞(JJ, JJR, JJS), 副詞(RB)それぞれのインデックスを保持
    pos_dict = defaultdict(list)
    for i, wp in enumerate(wps):
        w = wp[0]   # 単語
        p = wp[1]   # 品詞
        if p in ["VB", "VBD", "VBG", "VBM", "VBP", "VBZ"]:
            pos_dict['v'].append(i)
    
    hole_num = random.choice(pos_dict['v'])
    ans_word = words[hole_num]
    words[hole_num] = '<MASK>'

    return ' '.join(words), ans_word, hole_num


## 受け取った動詞を原形に変換する
def change2base(verb_word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(verb_word, pos='v')


## 動詞の原形から動詞の活用形リストを返す
def get_conjugated_verb_list(base_verb):
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


def return_Q_material(sentence_list):
    q_sentences = []        # 問題文を格納するリスト
    ans_words = []          # 答えの単語を格納するリスト
    options = []            # 問題の選択肢を格納するリスト
    for sent in sentence_list:
        words, wps = get_word_pos(sentence=sent)                      # 単語分割および品詞の取得を行う
        q_sent, ans_word = mask_sentence(words, wps)                  # 問題文となる動詞をマスクする。また、答えの単語も取得
        base_verb = change2base(ans_word)                             # 動詞の原形を取得する
        verb_list = get_conjugated_verb_list(base_verb)               # 単語の活用形を取得する

        option = random.sample(verb_list, 3)
        option.append(ans_word)
        option = random.shuffle(option)

        q_sentences.append(q_sent)
        ans_words.append(ans_word)
        options.append(option)

    return q_sentences, ans_words, options

if __name__ == '__main__':
    sentence_list = [
      "The IT department is currently working on a software upgrade that will improve the company's network security.",
      "According to the latest sales figures, the company's revenue has increased by 15% compared to the same period last year.",
      "The HR department is organizing a series of training sessions on workplace diversity and inclusion for all employees."
    ]

    return_Q_material(sentence_list)
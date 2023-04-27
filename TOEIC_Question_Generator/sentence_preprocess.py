import nltk
import random
from collections import defaultdict

def get_word_pos(sentence):
    words = nltk.word_tokenize(sentence)  # 単語分割
    wps = nltk.pos_tag(words)             # (単語, 品詞) のリスト : wps = word & pos の複数形

    return words, wps


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
    words[hole_num] = '<MASK>'

    return ' '.join(words)
    


def main(sentence_list):
    words, wps = get_word_pos(sentence=sentence_list[0])
    q_sent = mask_sentence(words, wps)

    print(q_sent)

if __name__ == '__main__':
    sentence_list = [
      "The IT department is currently working on a software upgrade that will improve the company's network security.",
      "According to the latest sales figures, the company's revenue has increased by 15% compared to the same period last year.",
      "The HR department is organizing a series of training sessions on workplace diversity and inclusion for all employees."
    ]

    main(sentence_list)
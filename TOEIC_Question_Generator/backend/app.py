from flask import Flask, jsonify
from flask_cors import CORS
from Verb_Q_generator import Verb_Q_generator
from sentence_store import extract_sentence, store_DB

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/')
def generate_sentence():
   ## ChatGPTで問題文を作成し、DBに格納
   sentences = store_DB()
   print(sentences)
   ## 生成された英文を取得できるようにしておく
   res_sentences = {
      "sentences": sentences 
   }

   return jsonify(res_sentences)


@app.route('/verb')
def provider_part5():
   ## DBより問題文を抽出
   sentence_list = []
   db_response = extract_sentence(3)

   for res in db_response:
      sentence_list.append(res[1])

   ## 問題文を作成
   VerbQGen = Verb_Q_generator()
   q_sentences, ans_words, options = VerbQGen.return_Q_material(sentence_list)
   question_api = {
      'questions': q_sentences,
      'answers': ans_words,
      'options': options
   }
   
   return jsonify(question_api)

if __name__ == '__main__':
   app.run(debug=True, port=5000)
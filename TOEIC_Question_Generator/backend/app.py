from flask import Flask, jsonify
from flask_cors import CORS
from verb_Q_generator import return_Q_material
from sentence_generator import sentences_provider

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/part5')
def provider_part5():
   sentence_list = sentences_provider()
   q_sentences, ans_words, options = return_Q_material(sentence_list)
   question_api = {
      'questions': q_sentences,
      'answers': ans_words,
      'options': options
   }
   
   return jsonify(question_api)

if __name__ == '__main__':
   app.run(debug=True, port=5000)
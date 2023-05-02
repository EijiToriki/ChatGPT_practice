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

# sentence_list = [
#   "The IT department is currently working on a software upgrade that will improve the company's network security.",
#   "According to the latest sales figures, the company's revenue has increased by 15% compared to the same period last year.",
#   "The HR department is organizing a series of training sessions on workplace diversity and inclusion for all employees."
# ]

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
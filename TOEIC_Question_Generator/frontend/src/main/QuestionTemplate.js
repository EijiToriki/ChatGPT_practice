import { useState } from 'react';
import './css/QuestionTemplate.css';
import AnswerDisplay from './QuestionParts/AnswerDisplay';
import AnswerButton from './QuestionParts/AnswerButton';
import OptionDisplay from './QuestionParts/OptionDisplay';
import QDisplay from './QuestionParts/QDisplay';

function QuestionTemplate({sentences, ansWords, options, qNum, setQNum}) {
  const [ansPush, setAnsPush] = useState(false)   // 回答ボタンを押したか否か
  const [userAns, setUserAns] = useState('')      // ラジオボタンの回答

  return (
    <>
      <div className='qDisplay'>
        <QDisplay sentence={sentences[qNum]} qNum={qNum} />
      </div>
      <div className='optionDisplay'>
        <OptionDisplay 
          option={options[qNum]}
          userAns={userAns} 
          setUserAns={setUserAns} 
        />
      </div>
      {
      !ansPush ?
        <div className='answerButton'>
          <AnswerButton setAnsPush={setAnsPush} />
        </div>
      : 
        <div className='answerDisplay'>
          {
            userAns === ansWords[qNum] ? 
              <h1 className='right'>正解！</h1> 
            : 
              <h1 className='wrong'>不正解…</h1>
          }
          <AnswerDisplay 
            ansWord={ansWords[qNum]} 
            setQNum={setQNum} 
            setAnsPush={setAnsPush} 
          />
        </div>
      }
    </>
  );
}

export default QuestionTemplate;
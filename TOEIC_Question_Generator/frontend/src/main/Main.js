import { useState } from 'react';
import './css/Main.css';
import QuestionTemplate from './QuestionTemplate';
import QEndTemplate from './QEndTemplate';

function Main({sentences, ansWords, options, setIsLoading, setQType, setQMaterial}) {
  const [qNum, setQNum] = useState(0)             // 問題番号
  const allQNum = sentences.length

  return (
    <>
      {
        qNum !== allQNum ?
          <QuestionTemplate
            sentences={sentences}
            ansWords={ansWords}
            options={options}
            qNum={qNum}
            setQNum={setQNum}
          />
        :
          <QEndTemplate 
            setIsLoading={setIsLoading}
            setQType={setQType}
            setQMaterial={setQMaterial} 
          />
      }
    </>
  );
}

export default Main;
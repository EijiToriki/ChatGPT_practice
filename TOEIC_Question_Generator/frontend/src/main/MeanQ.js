import { useState, useEffect } from 'react';
import './css/MeanQ.css';
import axios from 'axios';

import QuestionTemplate from './QuestionTemplate';
import QEndTemplate from './QEndTemplate';

const baseURL = "http://127.0.0.1:5000/"
function MeanQ() {
  const [qNum, setQNum] = useState(0)             // 問題番号
  const [isLoading, setIsLoading] = useState(false)
  const [qMaterial, setQMaterial] = useState([])
  // const allQNum = sentences.length
  const allQNum = 3

  // 問題の読み出し
  useEffect(() => {
    async function fetchQuestion(){
      const res = await axios.get(baseURL + "mean")
      console.log(res.data)
      setQMaterial(res.data)
      setIsLoading(true)
    }
    fetchQuestion()
  }, [])

  return (
    <>
      {
        isLoading ?
          qNum !== allQNum ?
            <QuestionTemplate
              sentences={qMaterial.questions}
              ansWords={qMaterial.answers}
              options={qMaterial.options}
              qNum={qNum}
              setQNum={setQNum}
            />
          :
            <QEndTemplate 
              setIsLoading={setIsLoading}
              setQMaterial={setQMaterial} 
            />
        :
          <div className='loading'>
            <h1>読み込み中...</h1>
          </div>
      }
    </>
  );
}

export default MeanQ;
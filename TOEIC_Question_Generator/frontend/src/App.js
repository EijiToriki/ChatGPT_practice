import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import Header from './header/Header';
import Main from './main/Main'
import TopPage from './toppage/TopPage';

const baseURL = "http://127.0.0.1:5000/"
function App() {
  const [qMaterial, setQMaterial] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [qType, setQType] = useState('')

  useEffect(() => {
    async function storeSentence(){
      const res = await axios.get(baseURL)
      console.log(res)
    }
    storeSentence()
  }, [])

  useEffect(() => {
    async function fetchQuestion(){
      const res = await axios.get(baseURL + "part5")
      setQMaterial(res.data)
      setIsLoading(true)
    }
    fetchQuestion()
  }, [qType])
  
  return (
    <>
      <Header />
      {
      qType === '' ?
        <TopPage setQType={setQType} />
      :
        isLoading ?
          <Main 
            sentences={qMaterial.questions} 
            ansWords={qMaterial.answers} 
            options={qMaterial.options}
            setIsLoading={setIsLoading}
            setQType={setQType}
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

export default App;

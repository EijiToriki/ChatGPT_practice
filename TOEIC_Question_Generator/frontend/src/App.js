import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import Header from './header/Header';
import Main from './main/Main'

const baseURL = "http://127.0.0.1:5000/part5"
function App() {
  const [qMaterial, setQMaterial] = useState([])
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    async function fetchQuestion(){
      const res = await axios.get(baseURL)
      setQMaterial(res.data)
      setIsLoading(true)
    }
    fetchQuestion()
  }, [])
  
  return (
    <>
      {isLoading ?
        <div>
          <Header />
          <Main sentences={qMaterial.questions} ansWords={qMaterial.answers} options={qMaterial.options} />
        </div>
      :
        <div className='loading'>
          <h1>読み込み中...</h1>
        </div>
      }
    </>
  );
}

export default App;

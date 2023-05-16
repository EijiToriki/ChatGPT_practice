import { BrowserRouter, Route } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import Header from './header/Header';
import TopPage from './toppage/TopPage';
import VerbQ from './main/VerbQ';

const baseURL = "http://127.0.0.1:5000/"
function App() {
  

  // DBに文章をストックする
  useEffect(() => {
    async function storeSentence(){
      const res = await axios.get(baseURL)
      console.log(res)
    }
    storeSentence()
  }, [])
  
  return (
    <BrowserRouter>
      <Header />
      <Route exact path="/">
        <TopPage />
      </Route>
      <Route path="/verb">
          <VerbQ />
      </Route>
    </BrowserRouter>
  );
}

export default App;

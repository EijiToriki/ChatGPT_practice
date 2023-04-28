import './App.css';
import Header from './header/Header';
import Main from './main/Main'

import { sentences, ansWords, options } from './sample_data.js';

function App() {
  return (
    <>
      <Header />
      <Main sentences={sentences} ansWords={ansWords} options={options} />
    </>
  );
}

export default App;

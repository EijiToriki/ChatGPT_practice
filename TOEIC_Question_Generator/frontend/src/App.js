import { BrowserRouter, Route } from 'react-router-dom';
import './App.css';
import Header from './header/Header';
import TopPage from './toppage/TopPage';
import VerbQ from './main/VerbQ';
import MeanQ from './main/MeanQ';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Route exact path="/">
        <TopPage />
      </Route>
      <Route path="/verb">
          <VerbQ />
      </Route>
      <Route path="/mean">
          <MeanQ />
      </Route>
    </BrowserRouter>
  );
}

export default App;

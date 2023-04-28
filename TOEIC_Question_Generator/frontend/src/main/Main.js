import AnswerDisplay from './AnswerDisplay';
import OptionDisplay from './OptionDisplay';
import QDisplay from './QDisplay';
import './css/Main.css';

function Main({sentences, ansWords, options}) {
  return (
    <>
      <div className='qDisplay'>
        <QDisplay sentence={sentences[0]} />
      </div>
      <div className='optionDisplay'>
        <OptionDisplay option={options[0]} />
      </div>
      <div className='answerDisplay'>
        <AnswerDisplay ansWord={ansWords[0]} />
      </div>
    </>
  );
}

export default Main;
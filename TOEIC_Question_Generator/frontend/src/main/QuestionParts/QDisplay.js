import './css/QDisplay.css'

function QDisplay({sentence, qNum}) {
  return (
    <>
      <div className='qTitle'>
        Qestion{qNum + 1}
      </div>
      <div className='sentDisplay'>
        {sentence}
      </div>

    </>
  );
}

export default QDisplay;
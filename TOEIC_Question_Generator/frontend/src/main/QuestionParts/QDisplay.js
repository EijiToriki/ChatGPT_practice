import './css/QDisplay.css'

function QDisplay({sentence}) {
  return (
    <>
      <div className='qTitle'>
        Qestion1
      </div>
      <div className='sentDisplay'>
        {sentence}
      </div>

    </>
  );
}

export default QDisplay;
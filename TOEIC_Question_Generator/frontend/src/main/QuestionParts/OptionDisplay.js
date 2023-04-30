import './css/OptionDisplay.css'

function OptionDisplay({option, setUserAns}) {
  const changeRadio = (op) => {
    setUserAns(op)
  }
  return (
    <>
      <div className="radio-option">
        {
          option.map((op, idx) => {
            return(
              <label key={idx}>
                <input type="radio" name="radioOption" onChange={() => changeRadio(op)}/>
                {op}
              </label>
            )
          })
        }
      </div>
    </>
  );
}

export default OptionDisplay;
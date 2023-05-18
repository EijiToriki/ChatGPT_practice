import './css/OptionDisplay.css'

function OptionDisplay({option, userAns, setUserAns}) {
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
                <input 
                  type="radio"
                  value={op} 
                  name="radioOption" 
                  onChange={() => changeRadio(op)}
                  checked={op === userAns}
                />
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
import './css/OptionDisplay.css'
import Button from '@mui/material/Button';

function OptionDisplay({option}) {
  const handleButton = () => {
    console.log('push')
  }
  return (
    <>
      <div className="radio-option">
        {
          option.map((op, idx) => {
            return(
              <label key={idx}>
                <input type="radio" name="radioOption"/>
                {op}
              </label>
            )
          })
        }
      </div>
      <Button 
        variant="outlined" color='inherit' 
        style={{width: '150px', marginLeft: '21%'}} 
        onClick={() => handleButton()}
      >
        回答
      </Button>
    </>
  );
}

export default OptionDisplay;
import Button from '@mui/material/Button';

function AnswerButton({setAnsPush}) {
  const handleButton = () => {
    setAnsPush(true)
  }

  return(
    <Button 
    variant="outlined" color='inherit' 
    style={{width: '150px', marginLeft: '21%'}} 
    onClick={() => handleButton()}
    >
    回答
    </Button>
  )
}

export default AnswerButton;
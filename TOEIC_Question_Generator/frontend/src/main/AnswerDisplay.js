import { Grid } from '@mui/material';
import './css/AnswerDisplay.css'
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function AnswerDisplay({ansWord}) {
  const handleButton = () => {
    console.log('push')
  }
  return (
    <Grid
      container
      direction="column"
      spacing={0}
      alignItems="center"
      justify="center"
   >
        <Card sx={{ width: '300px', height: '80px' }}>
          <CardContent>
            <Typography variant="h5" component="div">
              答え
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary" fontSize="18px">
              {ansWord}
            </Typography>
          </CardContent>
        </Card>

        <Button 
          variant="outlined" color='success' 
          style={{width: '150px', marginTop: '20px'}} 
          onClick={() => handleButton()}
        >
          次の問題へ
        </Button>
    </Grid>
  );
}

export default AnswerDisplay;
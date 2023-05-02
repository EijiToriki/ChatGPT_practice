import './css/QEndTemplate.css';
import { Card, CardContent, Typography, CardActionArea } from '@mui/material';

function QEndTemplate({setIsLoading, setQType, setQMaterial}) {
  const backTopPage = () => {
    setIsLoading(false)
    setQType('')
    setQMaterial([])
  }

  return (
    <div className='end-card'>
      <Card sx={{ maxWidth: 345, margin: 'auto'}}>
        <CardActionArea onClick={() => backTopPage()}>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              TopPageへ
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </div>
  );
}

export default QEndTemplate;
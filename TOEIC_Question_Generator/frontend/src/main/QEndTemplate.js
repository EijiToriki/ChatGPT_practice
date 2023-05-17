import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import './css/QEndTemplate.css';
import { Card, CardContent, Typography, CardActionArea } from '@mui/material';

function QEndTemplate({setIsLoading, setQMaterial}) {
  const navigate = useHistory()

  const backTopPage = () => {
    setIsLoading(false)
    setQMaterial([])
    navigate.push('/')
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
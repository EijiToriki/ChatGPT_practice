import './css/TopPage.css';
import { Grid, Card, CardContent, CardActions, Button, Typography, } from '@mui/material';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

function TopPage() {
  const navigate = useHistory()

  const moveVerbQPage = () => {
    navigate.push('/verb')
  }

  const moveWordQPage = () => {

  }


  return (
    <div className='toppage'>
      <h3 className='toppage-direction'>問題の形式を選択せよ</h3>
      <Grid container spacing={3} alignItems='center' justifycontent='center'>
        <Grid item xs={6} >
          <Card sx={{ width: "50%", margin: 'auto'}} justifycontent='center'>
            <CardContent>
              <Typography variant="h5" component="div">
                動詞の活用形問題
              </Typography>
              <Typography variant="body2">
                主語・時制・能動/受動から、原形・三人称単数・分詞など
                <br />
                適切な形の動詞を選ぶ問題
              </Typography>
            </CardContent>
            <CardActions>
              <Button size='large' onClick={() => moveVerbQPage()}>問題へ</Button>
            </CardActions>
          </Card>
        </Grid>
        <Grid item xs={6}>
          <Card sx={{ width: "50%", margin: 'auto' }} justifycontent='center'>
            <CardContent>
              <Typography variant="h5" component="div">
                単語の意味問題
              </Typography>
              <Typography variant="body2">
                一文の意味を読み取り、同じ品詞で意味が異なる単語の選択肢から
                <br />
                適切な単語を選ぶ問題
              </Typography>
            </CardContent>
            <CardActions>
              <Button size='large' disabled onClick={() => moveWordQPage()}>Comming Soon</Button>
            </CardActions>
          </Card>
        </Grid>
      </Grid>
    </div>
  );
}

export default TopPage;

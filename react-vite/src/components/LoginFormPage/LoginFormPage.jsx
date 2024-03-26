import "./LoginForm.css";
import spotifyLogo from '../../media/spotifyLogo.png'
import {Link, useNavigate} from 'react-router-dom'

function LoginFormPage() {
    const navigate = useNavigate()

  return (
    <>
        <div className='loginPage'>
            <div id='loginTopBar'>
                <img id='spotifyLogo' src={spotifyLogo} alt={'Image of the Spotify logo'} onClick={() => navigate('/')}/>
            </div>
            <div id='loginFormCard'>
                <h1 id='loginTitle'>Login to Spotify</h1>
                <hr className='divider'/>
                <form id='loginForm'>
                    <label style={{background: 'none'}} htmlFor='email'>Email</label>
                    <input type='email' id='email' name='email' required placeholder='Enter your email'/>
                    <label style={{background: 'none'}} htmlFor='password'>Password:</label>
                    <input type='password' id='password' name='password' required placeholder='Enter your password'/>
                    <button id='loginSubmit' type='submit'>Login</button>
                </form>
                <hr className='divider'/>
                <p id='noAccountPrompt'>Don&apos;t have an account? <Link id='noAccountPromptLink' to='/signup'>Sign up for Spotify!</Link></p>
            </div>
        </div>
    </>
  );
}

export default LoginFormPage;

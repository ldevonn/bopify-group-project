import "./LoginForm.css";
import spotifyLogo from '../../media/spotifyLogo.png'
import {Navigate, Link, useNavigate} from 'react-router-dom'
import {useState} from "react";
import {thunkLogin} from "../../redux/session.js";
import {useSelector, useDispatch} from "react-redux";



function LoginFormPage() {
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const sessionUser = useSelector((state) => state.session.user)
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [errors, setErrors] = useState({})

    if (sessionUser) return <Navigate to="/" replace={true} />

    const handleSubmit = async (e) => {
        e.preventDefault()

        const serverResponse = await dispatch(
            thunkLogin({
                email,
                password
            })
        )
        if (serverResponse) {
            setErrors(serverResponse)
        } else {
            navigate('/')
        }
    }
  return (
    <>
        <div className='loginPage'>
            <div id='loginTopBar'>
                <img id='spotifyLogo' src={spotifyLogo} alt={'Image of the Spotify logo'} onClick={() => navigate('/')}/>
            </div>
            <div id='loginFormCard'>
                <h1 id='loginTitle'>Login to Spotify</h1>
                <hr className='divider'/>
                <form id='loginForm' onSubmit={handleSubmit}>
                    <label style={{background: 'none'}} htmlFor='email'>Email</label>
                    <input type='email' id='email' name='email' required placeholder='Enter your email' onChange={(e) => setEmail(e.target.value)}/>
                    {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}
                    <label style={{background: 'none'}} htmlFor='password'>Password:</label>
                    <input type='password' id='password' name='password' required placeholder='Enter your password' onChange={(e) => setPassword(e.target.value)}/>
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

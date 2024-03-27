import spotifyLogo from '../../media/spotifyLogo.png'
import './SignupForm.css'
import {Navigate, Link, useNavigate} from "react-router-dom";
import {useState} from "react";
import {thunkLogin} from "../../redux/session.js";
import {useSelector, useDispatch} from "react-redux";


function SignupFormPage() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState({})

  return (
      <>
        <div className='signupPage'>
          <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')}/>
          <div className='signupFormCard'>
            <h1 id='signupTitle'>Sign up to start listening</h1>
            <form id='signupForm'>
              <label style={{background: 'none'}} htmlFor='name'>Name</label>
              <p id='nameDesc'>This name will appear on your profile</p>
              <input type='name' id='name' name='name' required placeholder='Name'/>
              <label style={{background: 'none'}} htmlFor='email'>Email</label>
              <p id='emailDesc'>We need an email so we can keep you updated on new music!</p>
              <input type='email' id='emailSU' name='email' required placeholder='Email'/>
              <label style={{background: 'none'}} htmlFor='password'>Password:</label>
              <p id='passwordDesc'>We need this so that only you can access the account!</p>
              <input type='password' id='passwordSU' name='password' required placeholder='Password'/>
              <button id='loginSubmit' type='submit'>Signup</button>
              <hr className='dividerSU'/>
              <p id='signupAdditional'>Already have an account? <Link id='loginLnk' to='/login'>Log in to Spotify!</Link></p>
            </form>
          </div>
        </div>
      </>
  );
}

export default SignupFormPage;

import spotifyLogo from '../../media/spotifyLogo.png'
import './SignupForm.css'
import {Navigate, Link, useNavigate} from "react-router-dom";
import {useState} from "react";
import {thunkSignup} from "../../redux/session.js";
import {useSelector, useDispatch} from "react-redux";


function SignupFormPage() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState({})

  if (sessionUser) return <Navigate to="/" replace={true} />

  const handleSubmit = async (e) => {
    e.preventDefault()

    const serverResponse = await dispatch(
        thunkSignup({
          name,
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
        <div className='signupPage'>
          <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')}/>
          <div className='signupFormCard'>
            <h1 id='signupTitle'>Sign up to start listening</h1>
            <form id='signupForm' onSubmit={handleSubmit}>
              {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}
              <label style={{background: 'none'}} htmlFor='name'>Name</label>
              <p id='nameDesc'>This name will appear on your profile</p>
              <input type='name' id='name' name='name' required placeholder='Name' onChange={(e) => setName(e.target.value)}/>
              <label style={{background: 'none'}} htmlFor='email'>Email</label>
              <p id='emailDesc'>We need an email so we can keep you updated on new music!</p>
              <input type='email' id='emailSU' name='email' required placeholder='Email' onChange={(e) => setEmail(e.target.value)}/>
              <label style={{background: 'none'}} htmlFor='password'>Password:</label>
              <p id='passwordDesc'>We need this so that only you can access the account!</p>
              <input type='password' id='passwordSU' name='password' required placeholder='Password' onChange={(e) => setPassword(e.target.value)}/>
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

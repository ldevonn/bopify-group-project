import {useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import {thunkLogout} from "../../../redux/session";
import './TopNav.css'

function TopNav() {
    const navigate = useNavigate();
    const sessionUser = useSelector(state => state.session.user);
    const dispatch = useDispatch()

    function handleNav(route) {
        navigate(`${route}`);
    }

    const logOut = (e) => {
        e.preventDefault()
        dispatch(thunkLogout())
        navigate(`/`)
    }

    if (sessionUser) {
        return (
            <div id="topNavLoggedIn">
                <p id='welcomeMessage'>Welcome, {sessionUser.name}!</p>
                <button id='logoutButton' onClick={logOut}>Log Out</button>
            </div>
        )
    } else {
        return (
            <div id="topNav">
                <button id='signupButton' onClick={() => handleNav('/signup')}>Sign Up</button>
                <button id='loginButton' onClick={() => handleNav('/login')}>Log In</button>
            </div>
        )
    }

}

export default TopNav

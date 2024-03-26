import {useNavigate } from "react-router-dom";
import './TopNav.css'

function TopNav() {
    const navigate = useNavigate();

    function handleNav(route) {
        navigate(`${route}`);
    }

    return (
        <div id="topNav">
            <button id='signupButton' onClick={() => handleNav('/signup')}>Sign Up</button>
            <button id='loginButton' onClick={() => handleNav('/login')}>Log In</button>
        </div>
    )
}

export default TopNav
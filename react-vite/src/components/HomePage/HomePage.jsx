import spotifyLogo from '../../media/spotifyLogo.png'
import {useNavigate } from "react-router-dom";

import "./HomePage.css";

function HomePage() {
    const navigate = useNavigate();

    function handleNav(route) {
        navigate(`${route}`);
    }
    
    return (
        <>
        <div id='homePage'>
            <div id="topLeftNav">
                <img id="spotifyLogo" src={`${spotifyLogo}`}></img>
                <button id="homeButton">Home</button>
                <button id="searchButton">Search</button>
            </div>
            <div id="topNav">
                <button id='signupButton' onClick={() => handleNav('/signup')}>Sign Up</button>
                <button id='loginButton' onClick={() => handleNav('/login')}>Log In</button>
            </div>
        <h1 id='wip'>COMING SOON TO A SCREEN NEAR YOU</h1>
        </div>
        </>
    )
}

export default HomePage
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
        <div id="topLeftNav">
            <img id="spotifyLogo" src={`${spotifyLogo}`}></img>
            <button id="homeButton">Home</button>
            <button id="searchButton">Search</button>
        </div>
        <div id="topNav">
            <button id='signupButton' onClick={() => handleNav('/signup')}>Sign Up</button>
            <button id='loginButton' onClick={() => handleNav('/login')}>Log In</button>
        </div>
        <div id='leftNav'>
            <h1 id='leftNavTitle'>Your Library</h1>
            <div id='createPlaylistComp'>
                <p>Create your first playlist</p>
                <p>It's easy, we'll help you!</p>
                <button id='createPlaylistButton'>Create playlist</button>
            </div>
        </div>
        </>
    )
}

export default HomePage
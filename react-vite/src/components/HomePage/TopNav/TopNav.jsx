import {useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import {thunkLogout} from "../../../redux/session";
import { thunkLogin } from "../../../redux/session";
import './TopNav.css'
import {useState} from "react";

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

    const demoLogin = async (e) => {
        e.preventDefault()

        const serverResponse = await dispatch(
            thunkLogin({
                email: 'demo@gmail.com',
                password: 'password'
            })
        )
        if (!serverResponse) {
            navigate('/')
        }
    }

    const demoArtistLogin = async (e) => {
        e.preventDefault()

        const serverResponse = await dispatch(
            thunkLogin({
                email: 'john@mayer.com',
                password: 'password'
            })
        )
        if (!serverResponse) {
            navigate('/')
        }
    }


    if (sessionUser) {
        return (
            <div id="topNavLoggedIn">
                <p id='welcomeMessage'>Welcome, {sessionUser.name}!</p>
                {sessionUser && sessionUser.isArtist ? (
                <button id="manageAlbums" onClick={() => navigate('/albums/manage')}>Manage Albums</button>
                ) : (<div></div>)}
                <button id='logoutButton' onClick={logOut}>Log Out</button>
            </div>
        )
    } else {
        return (
            <div id="topNav">
                <div id='demo-login-buttons'>
                    <button id='demo-user-login' onClick={demoLogin}>Login as demo user</button>
                    <button id='demo-user-login' onClick={demoArtistLogin}>Login as John Mayer</button>
                </div>
                <button id='signupButton' onClick={() => handleNav('/signup')}>Sign Up</button>
                <button id='loginButton' onClick={() => handleNav('/login')}>Log In</button>
            </div>
        )
    }

}

export default TopNav

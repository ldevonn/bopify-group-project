import spotifyLogo from '../../../media/spotifyLogo.png'
import {useNavigate} from "react-router-dom";


import './TopLeftNav.css'
function TopLeftNav() {
    const navigate = useNavigate()
    return (
        <div id="topLeftNav">
            <img id="spotifyLogo" src={`${spotifyLogo}`} onClick={() => navigate('/')}></img>
            <button id="homeButton" onClick={() => navigate('/')}>Home</button>
            <button id="searchButton">Search</button>
        </div>
    )
}

export default TopLeftNav
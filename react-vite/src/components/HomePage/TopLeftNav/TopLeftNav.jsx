import spotifyLogo from '../../../media/spotifyLogo.png'
import { useSelector } from 'react-redux'
import { Navigate, Link, useNavigate } from 'react-router-dom'


import './TopLeftNav.css'
function TopLeftNav() {
    const sessionUser = useSelector((state) => state.session.user)
    return (
        <div id="topLeftNav">
            <Link exact to="/">
                <img id="spotifyLogo" src={`${spotifyLogo}`}></img>
            </Link>
            <Link exact to="/">
                <button id="homeButton">Home</button>
            </Link>
            <button id="searchButton">Search</button>
            <Link to="/albums/new">
                {sessionUser && sessionUser.isArtist && <button id="createAlbumButton">Create an Album</button>}
            </Link>
        </div>
    )
}

export default TopLeftNav
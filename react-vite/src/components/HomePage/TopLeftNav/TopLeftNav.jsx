import spotifyLogo from '../../../media/spotifyLogo.png'
import { useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'


import './TopLeftNav.css'
function TopLeftNav() {
    const navigate = useNavigate()
    const sessionUser = useSelector((state) => state.session.user)
    return (
        <div id="topLeftNav">
            <img id="spotifyLogo" src={`${spotifyLogo}`} onClick={() => navigate('/')}></img>
            <button id="homeButton" onClick={() => navigate('/')}>Home</button>
            <button id='creditsButton' onClick={() => navigate('/credits')}>Credits</button>
            {sessionUser && sessionUser.isArtist && <button id="createAlbumButton" onClick={() => navigate('/albums/new')}>Create an Album</button>}
        </div>
    )
}

export default TopLeftNav

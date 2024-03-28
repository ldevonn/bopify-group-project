import { useNavigate } from "react-router-dom"
import { useSelector } from "react-redux";
import "./LeftNav.css"

function LeftNav() {
    const navigate = useNavigate()
    const sessionUser = useSelector(state => state.session.user);

    const handleCreatePlaylist = (e) => {
        e.preventDefault()
        if (!sessionUser) {
            navigate('/login')
        } else {
            navigate('/playlists/new')
        }
    }

    return (
    <div id='leftNav'>
        <h1 id='leftNavTitle'>Your Library</h1>
        <div id='createPlaylistComp'>
            <p>Create your first playlist</p>
            <p>It's easy, we'&apos;ll help you!</p>
            <button id='createPlaylistButton' onClick={handleCreatePlaylist} >Create playlist</button>
        </div>
    </div>
    )
}

export default LeftNav

import { fetchPlaylistByCurrentUser } from "../../redux/playlists"
import { useSelector, useDispatch } from "react-redux"
import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import likedsongs from "../../media/likedsongs.png"
// import TopLeftNav from "../HomePage/TopLeftNav"
// import LeftNav from "../HomePage/LeftNav"
// import TopNav from "../HomePage/TopNav"
// import MusicPlayer from "../MusicPlayer/MusicPlayer"
import "./AllPlaylistsCurrentUser.css"

function AllPlaylists () {
    const sessionUser = useSelector(state => state.session.user);
    const usersPlaylists = useSelector(state => state.playlists.allPlaylists);
    const dispatch = useDispatch()
    const navigate = useNavigate()


    useEffect(() => {
        dispatch(fetchPlaylistByCurrentUser())
    }, [dispatch, sessionUser])

    // useEffect(() => {
    //     if (!sessionUser) {
    //         navigate('/login')
    //     }
    // }, [sessionUser, navigate])

    const handleCreatePlaylist = (e) => {
        e.preventDefault()
        if (!sessionUser) {
            navigate('/login')
        } else {
            navigate('/playlists/new')
        }
    }

    return (
        <>
            {sessionUser && usersPlaylists && Object.keys(usersPlaylists).length > 0 ? (
                <>
                    <button id='createPlaylistButton' onClick={handleCreatePlaylist} >Create playlist</button>
                    {/* Liked Songs */}
                    <div className="playlistTile" onClick={() => navigate(`/liked`)}>
                        <img src={`${likedsongs}`} className="playlist-image"></img>
                        <div className="playlist-tile-info">
                            <div className="playlistTilePlaylistName">Liked Songs</div>
                            <div className="playlist-and-username">
                                <div className="all-playlists-playlist-tag">Playlist</div>
                                <div className="dot"> • </div>
                                <div className="all-playlists-username">{sessionUser.name}</div>
                            </div>
                        </div>
                    </div>
                    <div id='allPlaylistTiles'>
                    {usersPlaylists && Object.keys(usersPlaylists).map(playlistId => {
                        return (
                            <div key={playlistId} className="playlistTile" onClick={() => navigate(`/playlists/${usersPlaylists[playlistId].id}`)}>
                                <img src={`${usersPlaylists[playlistId].imageUrl}`} className="playlist-image"></img>
                                <div className="playlist-tile-info">
                                    <div className="playlistTilePlaylistName">{usersPlaylists[playlistId].name}</div>
                                    <div className="playlist-and-username">
                                        <div className="all-playlists-playlist-tag">Playlist</div>
                                        <div className="dot"> • </div>
                                        <div className="all-playlists-username">{sessionUser.name}</div>
                                    </div>
                                </div>
                            </div>
                        )
                    })}
                    </div>
                </>
            ) : (
                <div id='createPlaylistComp'>
                    <p>Create your first playlist</p>
                    <p>It&apos;s easy, we&apos;ll help you!</p>
                    <button id='createPlaylistButton' onClick={handleCreatePlaylist} >Create playlist</button>
                </div>
            )}

        </>
    )
}

export default AllPlaylists

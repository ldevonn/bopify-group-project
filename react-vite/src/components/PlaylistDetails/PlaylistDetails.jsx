import { fetchGetPlaylistDetails } from "../../redux/playlists"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from 'react-router-dom'
import { useEffect } from "react"
import TopLeftNav from "../HomePage/TopLeftNav"
import LeftNav from "../HomePage/LeftNav"
import TopNav from "../HomePage/TopNav"
import MusicPlayer from "../MusicPlayer/MusicPlayer"
import DeleteElement from "../DeleteButtons/DeleteElement"
import { useNavigate } from "react-router-dom"
import "./PlaylistDetails.css"

function PlaylistDetails () {
    let { playlistId } = useParams()
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const sessionUser = useSelector((state) => state.session.user)
    playlistId = +playlistId
    const playlist = useSelector(state => state.playlists.playlistDetails);

    useEffect(() => {
        dispatch(fetchGetPlaylistDetails(playlistId))
    }, [dispatch, playlistId])

    let songsPlural = 'song'
    if (playlist && Object.keys(playlist.playlist.tracks).length > 1) {
        songsPlural = 'songs'
        // console.log('line 25: ', Object.keys(playlist))
    }

    console.log(playlistId)

    return (
        <div className="playlist-details-page">
            <div className="leftColumn">
                <TopLeftNav />
                <LeftNav />
            </div>
            <div className="top-nav-with-gradient">
                <TopNav />
                <div className="playlist-detail-info-section">
                    <img src={playlist && playlist.playlist.imageUrl} className="playlist-detail-image"></img>
                    <div className="playlist-detail-playlist-tag-name-and-info">
                        <div className="playlist-detail-playlist-tag">Playlist</div>
                        <div className="album-detail-album-type-and-name">
                            <div className="playlist-detail-album-name">{playlist && playlist.playlist.name}</div>
                            <div className='album-detail-artist-release-date-length'>
                                <img src={playlist && playlist.playlist.user.imageUrl} className="user-profile-pic"></img>
                                <div className="album-detail-artist-name">{playlist && playlist.playlist.user.name}</div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{playlist && Object.keys(playlist.playlist.tracks).length} {songsPlural}</div>
                            </div>
                        </div>
                        {sessionUser && playlist && sessionUser.id == playlist.playlist.userId ? (
                            <>
                                <DeleteElement id="deleteButton" playlistId={playlistId}/>
                                <button className="edit-playlist-button" onClick={() => navigate(`/playlists/${playlistId}/edit`)}>Edit</button>
                            </>
                        ) : (<div></div>)}
                    </div>
                </div>
                <div className="album-detail-tracks-list">
                    {playlist && Object.keys(playlist.playlist.tracks).map((trackNum, i) => {
                        const track = playlist.playlist.tracks[trackNum]
                        // console.log('line 55: ', track)
                        const minutes = Math.floor(track.duration / 60)
                        const seconds = track.duration % 60
                        return (
                            <div key={i} className="album-detail-track">
                                <div className="album-number-track-and-artist">
                                    <div className="album-detail-track-number">{i + 1}</div>
                                    <img className="playlist-track-images" src={track.albumImage} />
                                    <div className="album-detail-track-and-artist">
                                        <div className="playlist-detail-track-name">{track.name}</div>
                                        <div className="album-detail-track-artist">{track.artistName}</div>
                                    </div>
                                </div>
                                <div className="like-button-and-duration">
                                    <button className="album-detail-like-button">Like</button>
                                    <div className="album-detail-track-duration">{minutes}:{seconds}</div>
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>
            <div className="music-player">
                <MusicPlayer />
            </div>
        </div>
    )
}

export default PlaylistDetails

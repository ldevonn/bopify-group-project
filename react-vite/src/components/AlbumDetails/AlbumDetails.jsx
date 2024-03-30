import { fetchGetAlbumDetails } from "../../redux/albums"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from 'react-router-dom'
import { useEffect } from "react"
import TopLeftNav from "../HomePage/TopLeftNav"
import LeftNav from "../HomePage/LeftNav"
import TopNav from "../HomePage/TopNav"
import MusicPlayer from "../MusicPlayer/MusicPlayer"
// import { useNavigate } from "react-router-dom"
import "./AlbumDetails.css"

function AlbumDetails () {
    let { albumId } = useParams()
    const dispatch = useDispatch()
    albumId = +albumId
    const album = useSelector(state => state.albums.albumDetails);

    useEffect(() => {
        dispatch(fetchGetAlbumDetails(albumId))
    }, [dispatch, albumId])

    let songsPlural = 'song'
    if (album && album.tracks.length > 1) {
        songsPlural = 'songs'
    }

    return (
        <div className="album-details-page">
            <div className="leftColumn">
                <TopLeftNav />
                <LeftNav />
            </div>
            <div className="top-nav-with-gradient">
                <TopNav />
                <div className="album-detail-info-section">
                    <img src={album && album.imageUrl} className="album-detail-image"></img>
                    <div className="album-detail-type-name-and-info">
                        <div className="album-detail-album-type">{album && album.albumType}</div>
                        <div className="album-detail-album-type-and-name">
                            <div className="album-detail-album-name">{album && album.name}</div>
                            <div className='album-detail-artist-release-date-length'>
                                <img src={album && album.artist.imageUrl} className="artist-profile-pic"></img>
                                <div className="album-detail-artist-name">{album && album.artist.name}</div>
                                <div className="spacer-10px"></div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{album && album.releaseDate.slice(12, 16)}</div>
                                <div className="spacer-10px"></div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{album && album.tracks.length} {songsPlural}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="album-detail-tracks-list">
                    {album && album.tracks.map((track, i) => {
                        const minutes = Math.floor(track.duration / 60)
                        const seconds = track.duration % 60
                        return (
                            <div key={i} className="album-detail-track">
                                <div className="album-number-track-and-artist">
                                    <div className="album-detail-track-number">{i + 1}</div>
                                    <div className="album-detail-track-and-artist">
                                        <div className="album-detail-track-name">{track.name}</div>
                                        <div className="album-detail-track-artist">{album.artist.name}</div>
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

export default AlbumDetails

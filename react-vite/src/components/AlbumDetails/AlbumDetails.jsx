import { fetchGetAlbumDetails } from "../../redux/albums"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from 'react-router-dom'
import {useEffect, useState} from "react"
import TopLeftNav from "../HomePage/TopLeftNav"
import LeftNav from "../HomePage/LeftNav"
import TopNav from "../HomePage/TopNav"
import MusicPlayer from "../MusicPlayer/MusicPlayer"
import {likeTheTrack} from "../../redux/likes.js";
import {removeLikedTrack} from "../../redux/likes.js";

import "./AlbumDetails.css"

function AlbumDetails () {
    let { albumId } = useParams()
    const dispatch = useDispatch()
    albumId = +albumId
    const album = useSelector(state => state.albums.albumDetails);
    const [isLiked, setIsLiked] = useState(false)

    useEffect(() => {
        dispatch(fetchGetAlbumDetails(albumId))
    }, [dispatch, albumId])

    let songsPlural = 'song'
    if (album && album.tracks.length > 1) {
        songsPlural = 'songs'
    }

    async function toggleLike(trackId) {
        let likeButton = document.getElementById('likeButton')
        if (likeButton && !isLiked) {
            setIsLiked(true)
            likeButton.classList.remove('fa-regular')
            likeButton.classList.add('fa-solid')
            await dispatch(likeTheTrack(trackId))
        } else {
            setIsLiked(false)
            likeButton.classList.remove('fa-solid')
            likeButton.classList.add('fa-regular')
            await dispatch(removeLikedTrack(trackId))
        }
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
                        console.log(track)
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
                                    <i className="fa-regular fa-heart" id='likeButton' style={{background: 'transparent', marginRight: 10}} onClick={() => toggleLike(track.trackId)}></i>
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

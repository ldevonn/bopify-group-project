import { fetchGetLikedTracksByCurrentUser } from "../../redux/likes"
import { useSelector, useDispatch } from "react-redux"
import { useEffect, useState } from "react"
import { likeTheTrack, removeLikedTrack } from "../../redux/likes.js";
import TopLeftNav from "../HomePage/TopLeftNav"
import LeftNav from "../HomePage/LeftNav"
import TopNav from "../HomePage/TopNav"
import MusicPlayer from "../MusicPlayer/MusicPlayer"
import likedsongs from "../../media/likedsongs.png"
import "./LikedTracks.css"

function LikedTracks () {
    const dispatch = useDispatch()
    // const navigate = useNavigate()
    const user = useSelector(state => state.session.user);
    const likes = useSelector(state => state.likes.userLikedTracks);

    const [track, setTrack] = useState(undefined)
    const [isLiked, setIsLiked] = useState(false);
    const [trackId, setTrackId] = useState(null)

    useEffect(() => {
        dispatch(fetchGetLikedTracksByCurrentUser())
    }, [dispatch])

    async function toggleLike(trackId) {
        let likeButton = document.getElementById(`likeButton-${trackId}`);
        if (likeButton && !isLiked) {
            setIsLiked(true);
            likeButton.classList.remove('fa-regular');
            likeButton.classList.add('fa-solid');
            await dispatch(likeTheTrack(trackId));
        } else {
            setIsLiked(false);
            likeButton.classList.remove('fa-solid');
            likeButton.classList.add('fa-regular');
            await dispatch(removeLikedTrack(trackId));
        }
    }

    function handlePlay(track, i) {
        const audio = new Audio(track.file)
        setTrack(audio)
        setTrackId(i)
    }

    function handleNext(){
        let nextSongIndex = trackId + 1;
        if (nextSongIndex >= likes.length){
            nextSongIndex = 0
        }
        const nextSong = likes[nextSongIndex];
        handlePlay(nextSong, nextSongIndex)
    }

    let songsPlural = 'songs'
    if (likes && likes.length === 1) {
        songsPlural = 'song'
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
                    <img src={`${likedsongs}`} className="album-detail-image" alt="Album Cover"></img>
                    <div className="album-detail-type-name-and-info">
                    <div className="playlist-detail-playlist-tag">Playlist</div>
                        <div className="album-detail-album-type-and-name">
                            <div className="likes-detail-title">Liked Songs</div>
                            <div className='album-detail-artist-release-date-length'>
                                <img src={user && user.imageUrl} className="artist-profile-pic" alt="Artist Profile"></img>
                                <div className="album-detail-artist-name">{user && user.name}</div>
                                <div className="spacer-10px"></div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{likes && likes.length} {songsPlural}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="album-detail-tracks-list">
                    {likes && likes.map((track, i) => {
                        const minutes = Math.floor(track.duration / 60);
                        const seconds = track.duration % 60;
                        return (
                            <div key={i} className="album-detail-track" onDoubleClick={() => handlePlay(track, i)}>
                                <div className="album-number-track-and-artist">
                                    <div className="album-detail-track-number">{i + 1}</div>
                                    <div className="album-detail-track-and-artist">
                                        <div className="album-detail-track-name">{track.name}</div>
                                        <div className="album-detail-track-artist">{track.artistName}</div>
                                    </div>
                                </div>
                                <div className="like-button-and-duration">
                                    <i className="fa-regular fa-heart" id={`likeButton-${track.trackId}`} style={{background: 'transparent', marginRight: 10}} onClick={() => toggleLike(track.trackId)}></i>
                                    <div className="album-detail-track-duration">{minutes}:{seconds}</div>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
            <div className="music-player">
                <MusicPlayer
                    currAudio={track}
                    currAudioId={trackId}
                    likedSongs={likes}
                    handlePlayNext={handleNext}
                />
            </div>
        </div>
    );
}

export default LikedTracks

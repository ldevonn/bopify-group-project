import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from 'react-router-dom';
import { fetchGetAlbumDetails } from "../../redux/albums";
import { likeTheTrack, removeLikedTrack } from "../../redux/likes.js";
import DeleteElement from "../DeleteButtons/DeleteElement.jsx";
import TopLeftNav from "../HomePage/TopLeftNav";
import LeftNav from "../HomePage/LeftNav";
import TopNav from "../HomePage/TopNav";
import MusicPlayer from "../MusicPlayer/MusicPlayer";
import "./AlbumDetails.css";

function AlbumDetails() {
    let { albumId } = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate()
    albumId = +albumId;
    const album = useSelector(state => state.albums.albumDetails);
    const [isLiked, setIsLiked] = useState(false);
    const sessionUser = useSelector((state) => state.session.user)

    const [isPlaying, setIsPlaying] = useState(false)
    const [track, setTrack] = useState(undefined)


    useEffect(() => {
        dispatch(fetchGetAlbumDetails(albumId));
    }, [dispatch, albumId]);

    let songsPlural = 'song';
    if (album && album.tracks.length > 1) {
        songsPlural = 'songs';
    }

    async function toggleLike(trackId) {
        let likeButton = document.getElementById('likeButton');
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

    function handlePlay(audioFile) {
        console.log(audioFile)
        if (!isPlaying) {
            const audio = new Audio(audioFile)
            audio.onloadedmetadata = () => {
                audio.play()
                setIsPlaying(true)
                setTrack(audio)
            }
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
                    <img src={album && album.imageUrl} className="album-detail-image" alt="Album Cover"></img>
                    <div className="album-detail-type-name-and-info">
                        <div className="album-detail-album-type">{album && album.albumType}</div>
                        <div className="album-detail-album-type-and-name">
                            <div className="album-detail-album-name">{album && album.name}</div>
                            <div className='album-detail-artist-release-date-length'>
                                <img src={album && album.artist.imageUrl} className="artist-profile-pic" alt="Artist Profile"></img>
                                <div className="album-detail-artist-name">{album && album.artist.name}</div>
                                <div className="spacer-10px"></div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{album && album.releaseDate.slice(12, 16)}</div>
                                <div className="spacer-10px"></div>
                                <div className="dot"> • </div>
                                <div className="spacer-10px"></div>
                                <div className="album-detail-lighter-larger">{album && album.tracks.length} {songsPlural}</div>
                                {sessionUser && album && sessionUser.id == album.artistId ? (
                                    <button className="add-song-button" onClick={() => navigate(`/albums/${albumId}/tracks/new`)}>Add a Song</button>
                                ) : <div></div>}
                            </div>
                        </div>
                    </div>
                </div>
                <div className="album-detail-tracks-list">
                    {album && album.tracks.map((track, i) => {
                        const minutes = Math.floor(track.duration / 60);
                        const seconds = track.duration % 60;
                        return (
                            <div key={i} className="album-detail-track" onDoubleClick={() => handlePlay(track.file)}>
                                <div className="album-number-track-and-artist">
                                    <div className="album-detail-track-number">{i + 1}</div>
                                    <div className="album-detail-track-and-artist">
                                        <div className="album-detail-track-name">{track.name}</div>
                                        <div className="album-detail-track-artist">{album.artist.name}</div>
                                    </div>
                                </div>
                                <div className="like-button-and-duration">
                                    {sessionUser && album && sessionUser.id == album.artistId ? (
                                        <DeleteElement trackId={track.trackId} albumIdForNav={albumId}/>
                                    ) : <div></div>}
                                    <i className="fa-regular fa-plus" id='plusButton' onClick={() => navigate(`/playlists/addTrack/${track.trackId}`)}></i>
                                    <i className="fa-regular fa-heart" id='likeButton' style={{background: 'transparent', marginRight: 10}} onClick={() => toggleLike(track.trackId)}></i>
                                    <div className="album-detail-track-duration">{minutes}:{seconds}</div>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
            <div className="music-player">
                <MusicPlayer isPlaying={isPlaying} currAudio={track}/>
            </div>
        </div>
    );
}

export default AlbumDetails;

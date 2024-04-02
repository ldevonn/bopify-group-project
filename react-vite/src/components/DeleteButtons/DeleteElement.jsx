import { useState } from 'react';
import {useDispatch} from "react-redux";
import {fetchDeletePlaylist} from '../../redux/playlists.js'
import {fetchDeleteAlbum} from '../../redux/albums.js'
import { fetchDeleteTrack } from '../../redux/tracks.js';
import { fetchDeleteFromPlaylist } from '../../redux/playlists.js';
import { useNavigate } from 'react-router-dom';
import './DeleteElement.css';

function DeleteElement(props) {
    const [isImageRed, setIsImageRed] = useState(false); // State to track image color
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const currentUrl = window.location.pathname

    const handleClick = async () => {
        if (!isImageRed) {
            setIsImageRed(true); // Toggle image color between black and red
        } else {
            try {
                console.log("line 20: ", props)
                if (props.albumId) await handleDelete(props.albumId)
                if (props.playlistId) await handleDelete(props.playlistId, props.albumId, props.deletePlaylistTrack)
                if (props.trackId) await handleDelete(props.trackId, props.albumIdForNav)
                if (props.playlistTrackId) await handleDelete(props.playlistTrackId, props.albumId, props.deletePlaylistTrack, props.playlistTrackDeleteId)
                navigate('/')
            } catch (error) {
                console.error('Error deleting element:', error)
            }
        }
    };

    const handleDelete = async (elementId, albumId, deletePlaylistTrack, playlistId) => {
        // console.log("HIT!!!!!!!!!!!!!!!!!", elementId, playlistId)
        // console.log("elementId: ", elementId)
        // console.log("playlistId: ", playlistId)
        // console.log("deletePlaylistTrack: ", deletePlaylistTrack)
        // console.log(currentUrl)
        try {
            if (!deletePlaylistTrack && currentUrl === `/playlists/${elementId}`) {
                console.log('Line 19:', elementId)
                await dispatch(fetchDeletePlaylist(elementId))
            } else if (currentUrl === '/albums/manage') {
                await dispatch(fetchDeleteAlbum(elementId))
            } else if (currentUrl === `/albums/${albumId}`)  {
                await dispatch(fetchDeleteTrack(elementId))
            } else if (deletePlaylistTrack && currentUrl === `/playlists/${playlistId}`)  {
                console.log("HIT!!!!!!!!!!!!!!!!!", elementId, playlistId)
                await dispatch(fetchDeleteFromPlaylist(elementId, playlistId))
            } else {
                console.log('current url not supported')
            }
        } catch (error) {
            console.error('Error deleting element:', error)
        }
    }

    return (
        <>
            <div className='delete-playlist-comp'>
                <div
                    id='delete-playlist-img'
                    className={isImageRed ? 'red-image' : ''}
                    onClick={handleClick}
                >
                    <i className="fa-solid fa-delete-left"></i>
                </div>
            </div>
        </>
    );
}

export default DeleteElement;

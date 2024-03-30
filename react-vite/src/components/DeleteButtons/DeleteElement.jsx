import { useState } from 'react';
import {useDispatch} from "react-redux";
import {fetchDeletePlaylist} from '../../redux/playlists.js'
import {fetchDeleteAlbum} from '../../redux/albums.js'
import './DeleteElement.css';

function DeleteElement() {
    const [isImageRed, setIsImageRed] = useState(false); // State to track image color
    const dispatch = useDispatch()
    const currentUrl = window.location.pathname

    const handleClick = async () => {
        if (!isImageRed) {
            setIsImageRed(true); // Toggle image color between black and red
        } else {
            try {
                await handleDelete()
            } catch (error) {
                console.error('Error deleting element:', error)
            }
        }
    };

    const handleDelete = async (elementId) => {
        try {
            if (currentUrl === '/testing') {
                await dispatch(fetchDeletePlaylist(elementId))
            } else if (currentUrl === '/album/delete') {
                await dispatch(fetchDeleteAlbum(elementId))
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

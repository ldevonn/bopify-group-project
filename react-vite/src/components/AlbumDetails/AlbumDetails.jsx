import { fetchGetAlbumDetails } from "../../redux/albums"
import { useSelector, useDispatch } from "react-redux"
import { useParams } from 'react-router-dom'
import { useEffect } from "react"
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

    // artist =

    return (
        <div className="album-detail-info-section">
            <img src={album && album.imageUrl} className="album-detail-image"></img>
            <div className="album-detail-type-name-and-info">
                <div className="album-detail-album-type">{album && album.albumType}</div>
                <div className="album-detail-album-name">{album && album.name}</div>
                <div className='album-detail-artist-release-date-length'>
                    <div>{album && album.artist.name}</div>
                    <div>•</div>
                    <div>{album && album.releaseDate.slice(12, 16)}</div>
                    <div>•</div>
                    <div>{album && album.tracks.length} songs</div>
                </div>
            </div>
        </div>
    )
}

export default AlbumDetails

import { fetchGetAlbums } from "../../../redux/albums"
import { useSelector, useDispatch } from "react-redux"
import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "./AllAlbums.css"

function AllAlbums () {
    const allAlbums = useSelector(state => state.albums.allAlbums);
    const dispatch = useDispatch()
    const navigate = useNavigate()

    useEffect(() => {
        dispatch(fetchGetAlbums())
    }, [dispatch])

    console.log("Hit!!!", allAlbums)

    return (
        <div id='allAlbumTiles'>
            {allAlbums && allAlbums.albums.map(album => {
                return (
                    <div key={album.id} className="albumTile" onClick={() => navigate(`/albums/${album.albumId}`)}>
                        <img src={`${album.imageUrl}`} className="album-image"></img>
                        <div className="albumTileAlbumName">{album.name}</div>
                        <div className="albumTileArtistName">{album.artistName}</div>
                    </div>
                )
            })}
        </div>
    )
}

export default AllAlbums

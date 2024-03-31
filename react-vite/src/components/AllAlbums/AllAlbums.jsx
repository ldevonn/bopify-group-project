import { fetchGetAlbums } from "../../redux/albums"
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

    return (
        <>
        <h1 className="all-albums-title">All Albums</h1>
        <div id='allAlbumTiles'>
            {allAlbums && allAlbums.albums.map((album, i) => {
                return (
                    <div key={i} className="albumTile" onClick={() => navigate(`/albums/${album.albumId}`)}>
                        <img src={`${album.imageUrl}`} className="album-image"></img>
                        <div className="albumTileAlbumName">{album.name}</div>
                        <div className="albumTileArtistName">{album.artistName}</div>
                    </div>
                )
            })}
        </div>
        </>
    )
}

export default AllAlbums

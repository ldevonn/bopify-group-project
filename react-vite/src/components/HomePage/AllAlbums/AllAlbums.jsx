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

    console.log("HIT!!!", allAlbums)

    return (
        <div id='allAlbumTiles'>
            {allAlbums && allAlbums.albums.map(album => {
                return (
                    <div key={album.id} className="albumTile">
                        <img src={`${album.imageUrl}`} className="album-image"></img>
                        <div className="albumTileText">{album.name}</div>
                        <div className="albumTileText">artistId: {album.artistId}</div>
                    </div>
                )
            })}
        </div>
    )
}

export default AllAlbums

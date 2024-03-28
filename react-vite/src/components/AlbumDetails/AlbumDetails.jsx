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
    }, [dispatch])

    console.log(album)

    return (
        <h1>Album Details</h1>
    )
}

export default AlbumDetails

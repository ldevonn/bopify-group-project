import { fetchCurrentUserAlbums } from "../../redux/albums"
import { useSelector, useDispatch } from "react-redux"
import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import TopLeftNav from "../HomePage/TopLeftNav"
import LeftNav from "../HomePage/LeftNav"
import TopNav from "../HomePage/TopNav"
import MusicPlayer from "../MusicPlayer/MusicPlayer"
import "./ManageAlbums.css"
import DeleteElement from "../DeleteButtons/DeleteElement.jsx";

function ManageAlbums () {
    const sessionUser = useSelector(state => state.session.user);
    const usersAlbums = useSelector(state => state.albums.albumByArtist);
    const dispatch = useDispatch()
    const navigate = useNavigate()

    useEffect(() => {
        dispatch(fetchCurrentUserAlbums())
    }, [dispatch])

    useEffect(() => {
        if (!sessionUser) {
            navigate('/')
        }
    }, [sessionUser, navigate])

    return (
        <>
        <div className='homePage'>
            <div className="leftColumn">
                <TopLeftNav/>
                <LeftNav/>
            </div>
            <div className="top-nav-with-gradient">
                <TopNav/>
                <div id='allAlbumTiles'>
                    {usersAlbums && usersAlbums.map(album => {
                        return (
                            <div key={album.id} className="albumTile">
                                <img src={`${album.imageUrl}`} className="album-image"></img>
                                <div className="albumTileAlbumName">{album.name}</div>
                                <div className="edit-delete-album-buttons">
                                    <button className="placeholderEditbutton">Edit</button>
                                    <DeleteElement albumId={album.albumId}/>
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
        </>
    )
}

export default ManageAlbums

import AllPlaylists from "../../AllPlaylistsCurrentUser/AllPlaylistsCurrentUser";
import "./LeftNav.css"

function LeftNav() {

    return (
    <div id='leftNav'>
        <h1 id='leftNavTitle'>Your Library</h1>
        <AllPlaylists />
    </div>
    )
}

export default LeftNav

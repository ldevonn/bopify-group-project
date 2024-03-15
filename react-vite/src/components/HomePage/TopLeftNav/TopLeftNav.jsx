import spotifyLogo from '../../../media/spotifyLogo.png'


import './TopLeftNav.css'
function TopLeftNav() {
    return (
        <div id="topLeftNav">
            <img id="spotifyLogo" src={`${spotifyLogo}`}></img>
            <button id="homeButton">Home</button>
            <button id="searchButton">Search</button>
        </div>
    )
}

export default TopLeftNav
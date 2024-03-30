import TopNav from "./TopNav";
import LeftNav from './LeftNav'
import TopLeftNav from "./TopLeftNav";
import AllAlbums from "../AllAlbums";
import MusicPlayer from "../MusicPlayer/MusicPlayer";
import "./HomePage.css";

function HomePage() {
    return (
        <>
            <div className='homePage'>
                <div className="leftColumn">
                    <TopLeftNav/>
                    <LeftNav/>
                </div>
                <div className="top-nav-with-gradient">
                    <TopNav/>
                    <AllAlbums />
                </div>
                <div className="music-player">
                    <MusicPlayer />
                </div>
            </div>
        </>
    )
}

export default HomePage

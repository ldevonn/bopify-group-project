import TopNav from "./TopNav";
import LeftNav from './LeftNav'
import TopLeftNav from "./TopLeftNav";
import AllAlbums from "./AllAlbums";

import "./HomePage.css";

function HomePage() {
    return (
        <>
            <div className='homePage'>
                <div className="leftColumn">
                    <TopLeftNav/>
                    <LeftNav/>
                </div>
                <div className="top-nav-with-albums">
                    <TopNav/>
                    <AllAlbums/>
                </div>
            </div>
        </>
    )
}
export default HomePage

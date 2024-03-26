import TopNav from "./TopNav";
import LeftNav from './LeftNav'
import TopLeftNav from "./TopLeftNav";

import "./HomePage.css";

function HomePage() {
    return (
        <>
            <div className='homePage'>
                <div className="leftColumn">
                    <TopLeftNav/>
                    <LeftNav/>
                </div>
                <TopNav/>
            </div>
        </>
    )
}
export default HomePage

import TopNav from "./TopNav";
import LeftNav from './LeftNav'
import TopLeftNav from "./TopLeftNav";

import "./HomePage.css";

function HomePage() {
    return (
        <>
            <div className='homePage'>
                <TopLeftNav/>
                <LeftNav/>
                <TopNav/>
            </div>
        </>
    )
}
export default HomePage
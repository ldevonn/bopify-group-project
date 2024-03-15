import {useNavigate } from "react-router-dom";
import TopLeftNav from './TopLeftNav/TopLeftNav';
import LeftNav from "./LeftNav/LeftNav";
import TopNav from "./TopNav";

import "./HomePage.css";

function HomePage() {
    const navigate = useNavigate();

    function handleNav(route) {
        navigate(`${route}`);
    }
    
    return (
        <>
        <TopLeftNav/>
        <LeftNav/>
        <TopNav/>
        </>
    )
}

export default HomePage
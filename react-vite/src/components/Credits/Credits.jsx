import TopLeftNav from "../HomePage/TopLeftNav/TopLeftNav.jsx";
import LeftNav from "../HomePage/LeftNav/LeftNav.jsx";

import './Credits.css'
import {NavLink} from "react-router-dom";

function Credits () {

    return (
        <>
            <div className='main'>
                <div className='left'>
                    <TopLeftNav/>
                    <LeftNav/>
                </div>
                <div className='right'>
                    <div id='credits-wrapper'>
                        <h2 className={'text'}>Lars-Devon Nilsson</h2>
                        <NavLink className={'text'} to={'https://github.com/ldevonn'}>Github</NavLink>
                        <NavLink className={'text'} to={'https://www.linkedin.com/in/lars-devon-nilsson-1989781b0'}>Linkedin</NavLink>
                        <h2 className={'text'}>Andrew Streater</h2>
                        <NavLink className={'text'} to={'https://github.com/andrewstreater'}>Github</NavLink>
                        <NavLink className={'text'} to={'https://www.linkedin.com/in/andrewstreater/'}>Linkedin</NavLink>
                        <h2 className={'text'}>Anthony Hoang</h2>
                        <NavLink className={'text'} to={'https://github.com/ant-hoang'}>Github</NavLink>
                        <NavLink className={'text'} to={'https://www.linkedin.com/in/anthony-hoang-ab08ab97/'}>Linkedin</NavLink>
                        <h2 className={'text'}>Edward Jung</h2>
                        <NavLink className={'text'} to={'https://github.com/edwardhj'}>Github</NavLink>
                        <NavLink className={'text'} to={'https://www.linkedin.com/in/edwardhjung/'}>Linkedin</NavLink>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Credits

import './MusicPlayer.css'
import {useEffect, useState} from "react";



function MusicPlayer(props) {
    const [sliderValue, setSliderValue] = useState(0)
    const [isPlaying, setIsPlaying] = useState(false)

    const handleSliderChange = (e) => {
        setSliderValue(e.target.value)
    }

    useEffect(() => {
        let progress = document.getElementById('progressBar')

        if (props.isPlaying){
            setIsPlaying(true)
        }

        if (props.currAudio) {
            props.currAudio.onloadedmetadata = function (){
                progress.max = props.currAudio.duration;
                progress.value = props.currAudio.currentTime
            }
            props.currAudio.ontimeupdate = function () {
                progress.value = props.currAudio.currentTime
            }
            props.currAudio.onended = function () {
                setIsPlaying(false)
            }
            props.currAudio.onplay = function () {
                setIsPlaying(true)
            }
            props.currAudio.onpause = function () {
                setIsPlaying(false)
            }
        }

        progress.onchange = function () {
            props.currAudio.currentTime = progress.value;
            if (isPlaying) {
                props.currAudio.play();
            }
        };
    }, [props.currAudio, props.isPlaying, isPlaying])


    function playPause() {
        if (props.currAudio) {
            if (isPlaying) {
                props.currAudio.pause();
                setIsPlaying(false)
            } else {
                props.currAudio.play();
            }
        }
    }

    function rewind() {
        let playToggle = document.getElementById('play/stop')

        if (props.currAudio) {
            props.currAudio.currentTime = 0;
            if (isPlaying) {
                props.currAudio.start()
            }
        }
    }


    return (
        <>
            <div className='audioPage'>
                <input type="range"
                       id='progressBar'
                       value={sliderValue}
                       onChange={handleSliderChange}
                />
            </div>
            <div className='controls'>
                <div onClick={rewind}>
                    <i className="fa-solid fa-backward-fast"></i>
                </div>
                <div onClick={playPause}>
                    <i className={`fa-solid ${isPlaying ? 'fa-stop' : 'fa-play'}`} id='play/stop'></i>
                </div>
                <div>
                    <i className="fa-solid fa-forward-fast"></i>
                </div>
            </div>
        </>
    )
}

export default MusicPlayer;
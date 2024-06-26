import './MusicPlayer.css'
import {useEffect, useState} from "react";



function MusicPlayer(props) {
    const [sliderValue, setSliderValue] = useState(0)
    const [isPlaying, setIsPlaying] = useState(false)

    const handleSliderChange = (e) => {
        setSliderValue(e.target.value)
    }

    useEffect(() => {
        return () => {
            if (props.currAudio) {
                props.currAudio.pause()
            }
        }
    }, [props.currAudio])

    useEffect(() => {
        let progress = document.getElementById('progressBar')

        if (props.isPlaying){
            setIsPlaying(true)
        }

        if (props.currAudio) {
            props.currAudio.onloadedmetadata = function (){
                progress.max = props.currAudio.duration;
                progress.value = props.currAudio.currentTime
                props.currAudio.play()
            }
            props.currAudio.ontimeupdate = function () {
                progress.value = props.currAudio.currentTime
            }
            props.currAudio.onended = function () {
                props.handlePlayNext();
            }
            props.currAudio.onplay = function () {
                props.setIsPlaying(true)
            }
            props.currAudio.onpause = function () {
                props.setIsPlaying(false)
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
            if (props.isPlaying || isPlaying) {
                props.currAudio.pause();
                props.setIsPlaying(false)
                setIsPlaying(false)
            } else {
                props.currAudio.play();
                props.setIsPlaying(true)
                setIsPlaying(true)
            }
        }
    }

    function rewind() {
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
                    <i className={`fa-solid ${props.isPlaying ? 'fa-stop' : 'fa-play'}`} id='play/stop'></i>
                </div>
                <div onClick={props.handlePlayNext}>
                    <i className="fa-solid fa-forward-fast"></i>
                </div>
            </div>
        </>
    )
}

export default MusicPlayer;

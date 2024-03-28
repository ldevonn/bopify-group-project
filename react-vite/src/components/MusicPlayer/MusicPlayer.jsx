import demoSong from '../../media/music/SongDemo.mp3'
import './MusicPlayer.css'
import {useEffect, useState} from "react";



function MusicPlayer() {
    const [sliderValue, setSliderValue] = useState(0)
    const [isPlaying, setIsPlaying] = useState(false)

    const handleSliderChange = (e) => {
        setSliderValue(e.target.value)
    }

    useEffect(() => {
        let progress = document.getElementById('progressBar')
        let song = document.getElementById('song')

        if (song) {
            song.onloadedmetadata = function (){
                progress.max = song.duration;
                progress.value = song.currentTime
            }
            song.ontimeupdate = function () {
                progress.value = song.currentTime
            }
        }

        progress.onchange = function () {
            song.currentTime = progress.value;
            if (isPlaying) {
                song.play();
            }
        }
    }, [isPlaying])


    function playPause() {
        let playToggle = document.getElementById('play/stop')
        let song = document.getElementById('song')

        if (playToggle && song) {
            if(isPlaying){
                song.pause();
                setIsPlaying(false)
                playToggle.classList.remove("fa-stop")
                playToggle.classList.add("fa-play")
            } else {
                song.play()
                setIsPlaying(true)
                playToggle.classList.add("fa-stop")
                playToggle.classList.remove("fa-play")
            }
        }
    }

    function rewind() {
        let song = document.getElementById('song')
        let playToggle = document.getElementById('play/stop')

        if (playToggle && song) {
            song.currentTime = 0;
            if (isPlaying) {
                song.start()
            }
        }
    }


    return (
        <>
            <div className='audioPage'>
                <audio id="song">
                    <source src={demoSong} type="audio/mpeg"/>
                </audio>
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
                    <i className={"fa-solid fa-play"} id='play/stop'></i>
                </div>
                <div>
                    <i className="fa-solid fa-forward-fast"></i>
                </div>
            </div>
        </>
    )
}

export default MusicPlayer;
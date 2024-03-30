import { fetchGetLikedTracksByCurrentUser } from "../../redux/likes"
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "./LikedTracks.css"

function LikedTracks() {
  const likedTracks = useSelector(state => state.likes.userLikedTracks)
  const dispatch = useDispatch()
  const navigate = useNavigate()

  useEffect(() => {
    dispatch(fetchGetLikedTracksByCurrentUser())
  }, [dispatch])

  return (
    <div id='allLikedTracks'>
      {/* <h1 className='LIKEY'>LIKEY LIKEY</h1> */}
      {likedTracks && likedTracks.tracks.map((track, i) => {
        const minutes = Math.floor(track.duration / 60)  
        const seconds = track.duration % 60
        return (
          <div key={i} className="liked-detail-track">
            <div className="liked-number-track-and-artist">
              <div className="liked-detail-track-number">{i + 1}</div>
              <div className="liked-detail-track-and-artist">
                <div className="liked-detail-track-name">{track.name}</div>
              </div>
            </div>
            <div className="like-button-and-duration">
              <button className="liked-detail-like-button">Like</button>
              <div className="liked-detail-track-duration">{minutes}:{seconds}</div>
            </div>
          </div>
        )
      })}
    </div>
  )


}

export default LikedTracks
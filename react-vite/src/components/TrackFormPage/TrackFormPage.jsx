import spotifyLogo from '../../media/spotifyLogo.png'
import { createTrack } from '../../redux/tracks'
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { Navigate, useNavigate, useParams } from 'react-router-dom'
import "./TrackForm.css"

function TrackFormPage() {
  let { albumId } = useParams()
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user)
  const [name, setName] = useState('')
  const [duration, setDuration] = useState()
  const [file, setFile] = useState('')
  const [errors, setErrors] = useState({})

  if (!sessionUser || !sessionUser.isArtist) return <Navigate to="/" replace={true} />

  const handleSubmit = async (e) => {
    e.preventDefault()

    const formData = new FormData()
    formData.append("name", name)
    formData.append("duration", duration)
    formData.append("file", file)
    formData.append("albumId", albumId)

    const serverResponse = await dispatch(
      createTrack(formData)
    )
    if (serverResponse) {
      setErrors(serverResponse)
    } else {
      navigate('/')
    }
  }

  return (
    <>
      <div className='TrackFormPage'>
        <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')} />
        <div className='TrackFormCard'>
          <h1 id='TrackFormTitle'>Create your track</h1>
          <form id='TrackForm' onSubmit={handleSubmit} encType='multipart/form-data'>

            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}

            <label style={{ background: 'none' }} htmlFor='name'>Name</label>
            <input type='trackName' id='trackName' name='trackName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='duration'>Track Duration</label>
            <input type='text' id='duration' name='duration' required placeholder='duration' onChange={(e) => setDuration(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='trackFile'>Track File</label>
            <input type='file' accept='audio/*' id='trackFile' name='trackFile' onChange={(e) => setFile(e.target.files[0])}></input>

            <button id='trackSubmit' type='submit'>Create Track</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default TrackFormPage
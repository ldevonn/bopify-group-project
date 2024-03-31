import spotifyLogo from '../../media/spotifyLogo.png'
import { createPlaylist } from '../../redux/playlists';
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { Navigate, useNavigate } from 'react-router-dom'
import "./PlaylistForm.css"

function PlaylistFormPage() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user)
  const [name, setName] = useState('')
  const [imageUrl, setImageUrl] = useState('')
  const [isPrivate, setIsPrivate] = useState(false)
  const [errors, setErrors] = useState({})

  if (!sessionUser) return <Navigate to="/" replace={true} />

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (isPrivate == 'false') setIsPrivate(false)
    if (isPrivate == 'true') setIsPrivate(true)

    const formData = new FormData()
    formData.append("name", name)
    formData.append("imageUrl", imageUrl)
    formData.append("private", isPrivate)

    const serverResponse = await dispatch(
      createPlaylist(formData)
    )
    if (serverResponse) {
      setErrors(serverResponse)
    } else {
      navigate('/')
    }
  }

  return (
    <>
      <div className='playlistFormPage'>
        <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')} />
        <div className='playlistFormCard'>
          <h1 id='playlistFormTitle'>Create your playlist</h1>
          <form id='playlistForm' onSubmit={handleSubmit} encType='multipart/form-data'>

            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}

            <label className='playlist-form-name playlist-form-element' htmlFor='name'>Name</label>
            <input className='playlist-form-name playlist-form-element' type='playlistName' id='playlistName' name='playlistName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />

            <label className='playlist-form-element' htmlFor='playlistImageUrl'>Upload Image</label>
            <input className='playlist-form-element' type='file' accept='image/*' id='playlistImageUrl' name='playlistImageUrl' required placeholder='Upload Image' onChange={(e) => setImageUrl(e.target.files[0])} />

            <label className='playlist-form-element' htmlFor='isPrivate'>Is this a private playlist?</label>
            <select className='playlist-form-element' id='isPrivate' name='isPrivate' value={isPrivate} onChange={(e) => setIsPrivate(e.target.value)}>
              <option value={true}>Yes</option>
              <option value={false}>No</option>
            </select>

            <button className='playlistSubmit playlist-form-element' type='submit'>Create Album</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default PlaylistFormPage

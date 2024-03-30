import spotifyLogo from '../../media/spotifyLogo.png'
import { createPlaylist } from '../../redux/playlists';
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { Navigate, Link, useNavigate, NavLink } from 'react-router-dom'
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

    console.log({
        "name": name,
        "imageUrl": imageUrl,
        "private": isPrivate
      })

    const serverResponse = await dispatch(
      createPlaylist({
        "name": name,
        "imageUrl": imageUrl,
        "private": isPrivate
      })
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
          <form id='playlistForm' onSubmit={handleSubmit}>
            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}
            <label style={{ background: 'none' }} htmlFor='name'>Name</label>
            <input type='playlistName' id='playlistName' name='playlistName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />
            <label style={{ background: 'none' }} htmlFor='playlistImageUrl'>Image URL</label>
            <input type='text' id='playlistImageUrl' name='playlistImageUrl' required placeholder='Image Url' onChange={(e) => setImageUrl(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='isPrivate'>Is this a private playlist?</label>
            <select id='isPrivate' name='isPrivate' value={isPrivate} onChange={(e) => setIsPrivate(e.target.value)}>
              <option value={true}>Yes</option>
              <option value={false}>No</option>
            </select>
            <button id='playlistSubmit' type='submit'>Create Album</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default PlaylistFormPage
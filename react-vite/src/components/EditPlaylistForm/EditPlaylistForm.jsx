import spotifyLogo from '../../media/spotifyLogo.png'
import { updatePlaylist } from '../../redux/playlists';
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { Navigate, useNavigate, useParams } from 'react-router-dom'
import "./EditPlaylist.css"

function EditPlaylistForm() {
  let { playlistId } = useParams()
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
      updatePlaylist(formData, playlistId)
    )
    if (serverResponse) {
      setErrors(serverResponse)
    } else {
      navigate('/')
    }
  }

  return (
    <>
      <div className='editPlaylistFormPage'>
        <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')} />
        <div className='editPlaylistFormCard'>
          <h1 id='editPlaylistFormTitle'>Create your playlist</h1>
          <form id='editPlaylistForm' onSubmit={handleSubmit} encType='multipart/form-data'>

            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}

            <label style={{ background: 'none' }} htmlFor='name'>Name</label>
            <input type='playlistName' id='playlistName' name='playlistName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='playlistImageUrl'>Image URL</label>
            <input type='file' accept='image/*' id='playlistImageUrl' name='playlistImageUrl' required placeholder='Image Url' onChange={(e) => setImageUrl(e.target.files[0])} />

            <label style={{ background: 'none' }} htmlFor='isPrivate'>Is this a private playlist?</label>
            <select id='isPrivate' name='isPrivate' value={isPrivate} onChange={(e) => setIsPrivate(e.target.value)}>
              <option value={true}>Yes</option>
              <option value={false}>No</option>
            </select>

            <button id='playlistSubmit' type='submit'>Edit Album</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default EditPlaylistForm
import spotifyLogo from '../../media/spotifyLogo.png'
import { createAlbum } from "../../redux/albums";
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { Navigate, useNavigate } from 'react-router-dom'
import "./AlbumForm.css"

function AlbumFormPage () {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector((state) => state.session.user)
  const [name, setName] = useState('')
  const [releaseDate, setReleaseDate] = useState('')
  const [albumType, setAlbumType] = useState('Album')
  const [genre, setGenre] = useState('Rock')
  const [imageUrl, setImageUrl] = useState('')
  const [errors, setErrors] = useState({})

  if (!sessionUser) return <Navigate to="/" replace={true} />

  const handleSubmit = async (e) => {
    e.preventDefault()
    let date = new Date(releaseDate)
    let month = ''
    if (date.getMonth() < 9) {
      month = '0' + (date.getMonth() + 1)
    } else {
      month = (date.getMonth() + 1)
    }
    let fReleaseDate = (month + '/' + date.getDate() + '/' + date.getFullYear());

    const formData = new FormData()
    formData.append("name", name)
    formData.append("releaseDate", fReleaseDate)
    formData.append("albumType", albumType)
    formData.append("genre", genre)
    formData.append("imageUrl", imageUrl)
    
    const serverResponse = await dispatch(
      createAlbum(formData)
    )
    if (serverResponse) {
      setErrors(serverResponse)
    } else {
      navigate('/')
    }
  }

  return (
    <>
      <div className='albumFormPage'>
        <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')}/>
        <div className='albumFormCard'>
          <h1 id='albumFormTitle'>Create your album</h1>
          <form id='albumForm' onSubmit={handleSubmit} encType='multipart/form-data'>

            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}

            <label style={{ background: 'none' }} htmlFor='createAlbumName'>Name</label>
            <input type='text' id='createAlbumName' name='createAlbumName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />
            <label style={{ background: 'none' }} htmlFor='createReleaseDate'>Release Date</label>
            <input type='date' id='createReleaseDate' name='createReleaseDate' required placeholder='Release Date' onChange={(e) => setReleaseDate(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='createAlbumType'>Album Type</label>
            <select id='createAlbumType' name='createAlbumType' required value={albumType} onChange={(e) => setAlbumType(e.target.value)}>
              <option value='Album'>Album</option>
              <option value='Single'>Single</option>
            </select>

            <label style={{ background: 'none' }} htmlFor='createAlbumGenre'>Genre</label>
            <select id='createAlbumGenre' name='createAlbumGenre' required value={genre} onChange={(e) => setGenre(e.target.value)}>
              <option value='Rock'>Rock</option>
              <option value='Pop'>Pop</option>
              <option value='Hip hop'>Hip hop</option>
              <option value='Jazz'>Jazz</option>
              <option value='Blues'>Blues</option>
              <option value='Electronic'>Electronic</option>
              <option value='Folk'>Folk</option>
              <option value='R&B'>R&B</option>
              <option value='Country'>Country</option>
              <option value='Soul'>Soul</option>
              <option value='Funk'>Funk</option>
              <option value='Reggae'>Reggae</option>
              <option value='Latin'>Latin</option>
              <option value='Classical'>Classical</option>
              <option value='Electronic dance music (EDM)'>Electronic dance music (EDM)</option>
              <option value='Heavy metal'>Heavy metal</option>
              <option value='Alternative'>Alternative</option>
              <option value='Indie'>Indie</option>
              <option value='Punk'>Punk</option>
              <option value='Grunge'>Grunge</option>
              <option value='Country'>Country</option>
              <option value='Metal'>Metal</option>
              <option value='Alternative'>Alternative</option>
              <option value='Ska'>Ska</option>
              <option value='Reggae'>Reggae</option>
              <option value='Salsa'>Salsa</option>
              <option value='Afrobeat'>Afrobeat</option>
              <option value='Flamenco'>Flamenco</option>
              <option value='Bossa nova'>Bossa nova</option>
              <option value='Trance'>Trance</option>
              <option value='House'>House</option>
              <option value='Techno'>Techno</option>
              <option value='Drum and bass'>Drum and bass</option>
              <option value='Dubstep'>Dubstep</option>
              <option value='Trap'>Trap</option>
              <option value='Jungle'>Jungle</option>
              <option value='Glitch'>Glitch</option>
              <option value='Psychedeli'>Psychedelic</option>
            </select>

            <label style={{ background: 'none' }} htmlFor='createAlbumImage'>Image URL</label>
            <input type='file' accept='image/*' id='createAlbumImage' name='createAlbumImage' required placeholder='Image Url' onChange={(e) => setImageUrl(e.target.files[0])} />

            <button id='createAlbumSubmit' type='submit'>Create Album</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default AlbumFormPage
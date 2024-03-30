import spotifyLogo from '../../media/spotifyLogo.png'
import { updateAlbum } from "../../redux/albums";
import { useSelector, useDispatch } from "react-redux";
import { useState } from "react";
import { Navigate, useNavigate, useParams } from 'react-router-dom'
import "./EditAlbum.css"

function EditAlbumForm() {
  const navigate = useNavigate()
  const { albumId } = useParams()
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
      updateAlbum(formData, albumId)
    )
    if (serverResponse) {
      setErrors(serverResponse)
    } else {
      navigate('/')
    }
  }

  return (
    <>
      <div className='editAlbumFormPage'>
        <img id='spotifyLogo' src={spotifyLogo} onClick={() => navigate('/')} />
        <div className='editAlbumFormCard'>
          <h1 id='editAlbumFormTitle'>Update your album</h1>
          <form id='editAlbumForm' onSubmit={handleSubmit} encType='multipart/form-data'>


            {errors.length > 0 && errors.map((message) => <p key={message}>{message}</p>)}
            <label style={{ background: 'none' }} htmlFor='name'>Name</label>
            <input type='albumName' id='albumName' name='albumName' required placeholder='Name' onChange={(e) => setName(e.target.value)} />
            <label style={{ background: 'none' }} htmlFor='releaseDate'>Release Date</label>
            <input type='date' id='releaseDate' name='releaseDate' required placeholder='Release Date' onChange={(e) => setReleaseDate(e.target.value)} />

            <label style={{ background: 'none' }} htmlFor='albumType'>Album Type</label>
            <select id='albumType' name='albumType' required value={albumType} onChange={(e) => setAlbumType(e.target.value)}>
              <option value='Album'>Album</option>
              <option value='Single'>Single</option>
            </select>

            <label style={{ background: 'none' }} htmlFor='genre'>Genre</label>
            <select id='genre' name='genre' required value={genre} onChange={(e) => setGenre(e.target.value)}>
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

            <label style={{ background: 'none' }} htmlFor='imageUrl'>Image URL</label>
            <input type='file' accept='image/*' id='albumImageUrl' name='albumImageUrl' required placeholder='Image Url' onChange={(e) => setImageUrl(e.target.files[0])} />

            <button id='albumSubmit' type='submit'>Update Album</button>
          </form>
        </div>
      </div>
    </>
  )

}

export default EditAlbumForm
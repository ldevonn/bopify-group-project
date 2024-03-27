const GET_ALBUMS = 'albums/getAlbums'
const GET_ALBUM_DETAILS = 'albums/getAlbumDetails'
const GET_ALBUM_BY_ARTIST = 'albums/getAlbumByArtist'
const GET_ALBUM_BY_USER = 'albums/getAlbumByUser'
const ADD_ALBUM = 'albums/addAlbum'
const UPDATE_ALBUM = 'albums/updateAlbum'
const DELETE_ALBUM = 'albums/deleteAlbum'

const getAlbums = (allAlbums) => {
  return {
    type: GET_ALBUMS,
    allAlbums
  }
}

const getAlbumDetails = (albumDetails) => {
  return {
    type: GET_ALBUM_DETAILS,
    albumDetails
  }
}

const getAlbumByArtist = (albumByArtist) => {
  return {
    type: GET_ALBUM_BY_ARTIST,
    albumByArtist
  }
}

const getAlbumByCurrentUser = (albumByUser) => {
  return {
    type: GET_ALBUM_BY_USER,
    albumByUser
  }
}

const addAlbum = (newAlbum) => {
  return {
    type: ADD_ALBUM,
    newAlbum
  }
}

const modifiedAlbum = (updatedAlbum) => {
  return {
    type: UPDATE_ALBUM,
    updatedAlbum
  }
}

const deleteAlbum = (album) => {
  return {
    type: DELETE_ALBUM,
    album
  }
}

export const fetchGetAlbums = () => async (dispatch) => {
  const res = await fetch("/api/albums")
  if (res.ok) {
    const data = await res.json()
    const albumsData = {}

    for (let i = 0; i < data.albums.length; i++) {
      let currObj = data.albums[i]
      albumsData[currObj.id] = currObj
    }

    dispatch(getAlbums(albumsData))

    return albumsData
  }  else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchGetAlbumDetails = (albumId) => async (dispatch) => {
  const res = await fetch(`/api/albums/${albumId}`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getAlbumDetails(data))
    return data
  }  else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchAlbumByArtist = (artistId) => async (dispatch) => {
  const res = await fetch(`/api/albums/artists/${artistId}`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getAlbumByArtist(data))
    return data
  }  else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchCurrentUserAlbums = () => async (dispatch) => {
  const res = await fetch(`/api/albums/current`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getAlbumByCurrentUser(data))
    return data
  }  else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const createAlbum = (payload) => async (dispatch) => {
  const res = await fetch(`/api/albums`, {
    method: 'POST',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  
  if (res.ok) {
    const data = await res.json()
    dispatch(addAlbum(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const updateAlbum = (payload, albumId) => async (dispatch) => {
  const res = await fetch(`/api/albums/${albumId}`, {
    method: 'PUT',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  
  if (res.ok) {
    const data = await res.json()
    dispatch(modifiedAlbum(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchDeleteAlbum = (albumId) => async (dispatch) => {
  const res = await fetch(`api/albums/${albumId}`, {
    method: 'DELETE'
  })
  
  if (res.ok) {
    dispatch(deleteAlbum())
    return res
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

const albumsReducer = (state = {}, action) => {
  switch (action.type) {
    case GET_ALBUMS:
      return { ...state, allAlbums: action.allAlbums }
    case GET_ALBUM_DETAILS:
      return { ...state, albumDetails: action.albumDetails }
    case GET_ALBUM_BY_ARTIST:
      return { ...state, albumByArtist: action.albumByArtist }
    case GET_ALBUM_BY_USER:
      return { ...state, albumByArtist: action.albumByUser }
    case ADD_ALBUM:
      return { ...state, albumDetails: action.newAlbum }
    case UPDATE_ALBUM:
      return { ...state, albumDetails: action.modifiedAlbum }
    default:
      return state
  }
}

export default albumsReducer
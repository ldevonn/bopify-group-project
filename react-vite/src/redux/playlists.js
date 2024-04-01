const GET_PLAYLISTS_BY_CURRENT_USER = 'playlists/getPlaylistsByCurrentUser'
const GET_PLAYLIST_DETAILS = 'playlists/getPlaylistDetails'
const ADD_PLAYLIST = 'playlists/addPlaylist'
const UPDATE_PLAYLIST = 'playlists/updatePlaylist'
const DELETE_PLAYLIST = 'playlists/deletePlaylist'
const ADD_TO_PLAYLIST = 'playlists/addToPlaylist'

const getPlaylistsByCurrentUser = (allPlaylists) => {
  return {
    type: GET_PLAYLISTS_BY_CURRENT_USER,
    allPlaylists
  }
}

const getPlaylistDetails = (playlistDetails) => {
  return {
    type: GET_PLAYLIST_DETAILS,
    playlistDetails
  }
}

const addPlaylist = (newPlaylist) => {
  return {
    type: ADD_PLAYLIST,
    newPlaylist
  }
}

const modifiedPlaylist = (updatedPlaylist) => {
  return {
    type: UPDATE_PLAYLIST,
    updatedPlaylist
  }
}

const deletePlaylist = (playlist) => {
  return {
    type: DELETE_PLAYLIST,
    playlist
  }
}

const addToPlaylist = (data) => {
  return {
    type: ADD_TO_PLAYLIST,
    data
  }
}

export const fetchPlaylistByCurrentUser = () => async (dispatch) => {
  const res = await fetch("api/playlists/current")
  if (res.ok) {
    const data = await res.json()
    const playlistsData = {}

    for (let i = 0; i < data.playlists.length; i++) {
      let currObj = data.playlists[i]
      playlistsData[currObj.id] = currObj
    }

    dispatch(getPlaylistsByCurrentUser(playlistsData))

    return playlistsData
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchGetPlaylistDetails = (playlistId) => async (dispatch) => {
  const res = await fetch(`/api/playlists/${playlistId}`)
  if (res.ok) {
    const data = await res.json()
    dispatch(getPlaylistDetails(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const createPlaylist = (payload) => async (dispatch) => {
  const res = await fetch(`/api/playlists/new`, {
    method: 'POST',
    body: payload
  })

  if (res.ok) {
    const { resPost } = await res.json()
    dispatch(addPlaylist(resPost))
    return resPost
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const updatePlaylist = (payload, playlistId) => async (dispatch) => {
  const res = await fetch(`/api/playlists/${playlistId}`, {
    method: 'PUT',
    body: payload
  })

  if (res.ok) {
    const { resPost } = await res.json()
    dispatch(modifiedPlaylist(resPost))
    return resPost
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchDeletePlaylist = (playlistId) => async (dispatch) => {
  const res = await fetch(`/api/playlists/${playlistId}`, {
    method: 'DELETE'
  })

  if (res.ok) {
    dispatch(deletePlaylist())
    return res
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

export const fetchAddToPlaylist = (trackId, playlistId) => async (dispatch) => {
  const payload = {}
  const res = await fetch(`/api/playlists/${playlistId}/tracks/${trackId}`, {
    method: 'POST',
    header: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })

  if (res.ok) {
    const data = await res.json()
    dispatch(addToPlaylist(data))
    return data
  } else if (res.status < 500) {
    const errorMessages = await res.json()
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
}

const playlistsReducer = (state = {}, action) => {
  switch (action.type) {
    case GET_PLAYLISTS_BY_CURRENT_USER:
      return { ...state, allPlaylists: action.allPlaylists }
    case GET_PLAYLIST_DETAILS:
      return { ...state, playlistDetails: action.playlistDetails }
    case ADD_PLAYLIST:
      return { ...state, playlistDetails: action.newPlaylist }
    case UPDATE_PLAYLIST:
      return { ...state, playlistDetails: action.updatedPlaylist }
    case ADD_TO_PLAYLIST:
      return { ...state, playlistDetails: action.addToPlaylist}
    default:
      return state
  }
}

export default playlistsReducer
